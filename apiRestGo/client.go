package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Client struct {
	ID        string `json:"IdClient"`
	FirstName string `json:"prenom"`
	LastName  string `json:"nom"`
	Email     string `json:"email"`
}

var clients []Client
var cli Client

func getClients(w http.ResponseWriter, r *http.Request) {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		panic(err)
	}
	aff, err := db.Query("SELECT * FROM client")
	if err != nil {
		panic(err)
	}
	defer aff.Close()
	for aff.Next() {
		var client Client
		err := aff.Scan(&client.ID, &client.FirstName, &client.LastName, &client.Email)
		if err != nil {
			panic(err)
		}
		err = json.NewEncoder(w).Encode(client)
		if err != nil {
			panic(err)
		}
	}

	defer db.Close()

}

func handleClient(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		getClient(w, r)
	case "POST":
		createClient(w, r)
	case "PUT":
		updateClient(w, r)
	case "DELETE":
		deleteClient(w, r)
	default:
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}

func getClient(w http.ResponseWriter, r *http.Request) {

	id := getIdFromUrl(r.URL.Path)
	fmt.Println(id)
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
	}

	err = db.QueryRow("SELECT * FROM client WHERE IdClient = ?", id).Scan(&cli.ID, &cli.FirstName, &cli.LastName, &cli.Email)
	defer db.Close()
	if err != nil {
		http.Error(w, "Client not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(cli)

}

func createClient(w http.ResponseWriter, r *http.Request) {

	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
		return
	}

	ajout, err := db.Prepare("INSERT INTO client(firstname, lastname, email) VALUES(?, ?, ?)")
	if err != nil {
		log.Fatal(err)
		return
	}
	err = json.NewDecoder(r.Body).Decode(&cli)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	_, err = ajout.Exec(cli.FirstName, cli.LastName, cli.Email)
	if err != nil {
		log.Fatal(err)
		return
	}
	defer ajout.Close()
	defer db.Close()
	http.Error(w, "Client created", http.StatusCreated)

}

func updateClient(w http.ResponseWriter, r *http.Request) {
	id := getIdFromUrl(r.URL.Path)
	var updatedClient Client
	err := json.NewDecoder(r.Body).Decode(&updatedClient)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	for index, client := range clients {
		if client.ID == id {
			clients[index] = updatedClient
			json.NewEncoder(w).Encode(updatedClient)
			return
		}
	}
	http.Error(w, "Client not found", http.StatusNotFound)
}

func deleteClient(w http.ResponseWriter, r *http.Request) {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
		return
	}
	id := getIdFromUrl(r.URL.Path)
	delete, err := db.Prepare("DELETE FROM client WHERE IdClient = ?")
	if err != nil {
		log.Fatal(err)
		return
	}
	_, err = delete.Exec(id)
	if err != nil {
		log.Fatal(err)
		http.Error(w, "Client not found", http.StatusNotFound)
		return
	}
	http.Error(w, "Supression effectuer avec succes", http.StatusNotFound)
}

func getIdFromUrl(path string) string {
	id := path[len("/clients/"):]
	return id
}
