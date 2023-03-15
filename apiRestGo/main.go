package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("connexion reussie")

	http.HandleFunc("/clients", getClients)
	http.HandleFunc("/clients/", handleClient)
	// http.HandleFunc("/reservations", getReservations)
	// http.HandleFunc("/reservations/", handleReservation)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
