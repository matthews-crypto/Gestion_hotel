package main

import (
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	http.HandleFunc("/clients", getClients)
	http.HandleFunc("/clients/", handleClient)
	http.HandleFunc("/reservations", getReservations)
	http.HandleFunc("/reservations/", handleReservation)
	http.HandleFunc("/chambres", getChambres)
	http.HandleFunc("/chambres/", handleChambre)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
