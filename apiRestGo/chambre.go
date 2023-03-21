package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type chambre struct {
	ID        int    `json:"Idchambre"`
	FirstName string `json:"prenom"`
	LastName  string `json:"nom"`
	Email     string `json:"email"`
}

var cham chambre

func getChambres(w http.ResponseWriter, r *http.Request) {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		panic(err)
	}
	aff, err := db.Query("SELECT * FROM chambre")
	if err != nil {
		panic(err)
	}
	defer aff.Close()
	for aff.Next() {
		var chambre chambre
		err := aff.Scan(&chambre.ID, &chambre.FirstName, &chambre.LastName, &chambre.Email)
		if err != nil {
			panic(err)
		}
		err = json.NewEncoder(w).Encode(chambre)
		if err != nil {
			panic(err)
		}
	}

	defer db.Close()

}

func handleChambre(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		getchambre(w, r)
	case "POST":
		createchambre(w, r)
	case "PATCH":
		updatechambre(w, r)
	case "DELETE":
		deletechambre(w, r)
	default:
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}

func getchambre(w http.ResponseWriter, r *http.Request) {

	id := getIdFromUrl(r.URL.Path)
	fmt.Println(id)
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
	err = db.QueryRow("SELECT * FROM chambre WHERE Idchambre = ?", id).Scan(&cham.ID, &cham.FirstName, &cham.LastName, &cham.Email)

	if err != nil {
		http.Error(w, "chambre not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(cham)

}

func createchambre(w http.ResponseWriter, r *http.Request) {

	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
		return
	}
	defer db.Close()

	ajout, err := db.Prepare("INSERT INTO chambre(firstname, lastname, email) VALUES(?, ?, ?)")
	if err != nil {
		log.Fatal(err)
		return
	}
	err = json.NewDecoder(r.Body).Decode(&cham)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	_, err = ajout.Exec(cham.FirstName, cham.LastName, cham.Email)
	if err != nil {
		log.Fatal(err)
		return
	}
	defer ajout.Close()

	http.Error(w, "chambre created", http.StatusCreated)

}

func updatechambre(w http.ResponseWriter, r *http.Request) {
	// id := getIdFromUrl(r.URL.Path)
	// var updatedchambre chambre
	// err := json.NewDecoder(r.Body).Decode(&updatedchambre)
	// if err != nil {
	// 	http.Error(w, "Invalid request body", http.StatusBadRequest)
	// 	return
	// }
	// for index, chambre := range chambres {
	// 	if chambre.ID == id {
	// 		chambres[index] = updatedchambre
	// 		json.NewEncoder(w).Encode(updatedchambre)
	// 		return
	// 	}
	// }
	http.Error(w, "chambre not found", http.StatusNotFound)
}

func deletechambre(w http.ResponseWriter, r *http.Request) {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
		return
	}
	id := getIdFromUrl(r.URL.Path)
	delete, err := db.Prepare("DELETE FROM chambre WHERE Idchambre = ?")
	if err != nil {
		log.Fatal(err)
		return
	}
	_, err = delete.Exec(id)
	if err != nil {
		log.Fatal(err)
		http.Error(w, "chambre not found", http.StatusNotFound)
		return
	}
	http.Error(w, "Supression effectuer avec succes", http.StatusNotFound)
}
