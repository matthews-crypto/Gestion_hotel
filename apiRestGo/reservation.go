package main

import (
	"encoding/json"
	"net/http"
)

type Reservation struct {
	IdReservation    string `json:"idReservation"`
	date_reservation string `json:"date_reservation"`
	date_entree      string `json:"date_entree"`
	date_sortie      string `json:"date_sortie"`
	IdClient         string `json:"idClient"`
	IdChambre        string `json:idChambre`
	tarif            string `json:tarif`
}

var reservations []Reservation

func getReservations(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(reservations)
}
func handleReservation(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		getReservation(w, r)
	case "POST":
		createReservation(w, r)
	case "PUT":
		updateReservation(w, r)
	case "DELETE":
		deleteReservation(w, r)
	default:
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}
func getReservation(w http.ResponseWriter, r *http.Request) {
	id := getIdFromUrls(r.URL.Path)
	for _, reservation := range reservations {
		if reservation.IdReservation == id {

			json.NewEncoder(w).Encode(reservation)
			return
		}
	}
	http.Error(w, "Reservation not found", http.StatusNotFound)
}
func createReservation(w http.ResponseWriter, r *http.Request) {
	var reservation Reservation
	err := json.NewDecoder(r.Body).Decode(&reservation)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	reservations = append(reservations, reservation)
	json.NewEncoder(w).Encode(reservation)
}
func updateReservation(w http.ResponseWriter, r *http.Request) {
	id := getIdFromUrls(r.URL.Path)
	var updatedReservation Reservation
	err := json.NewDecoder(r.Body).Decode(&updatedReservation)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	for index, reservation := range reservations {
		if reservation.IdReservation == id {
			reservations[index] = updatedReservation
			json.NewEncoder(w).Encode(updatedReservation)
			return
		}
	}
	http.Error(w, "Reservation not found", http.StatusNotFound)
}

func deleteReservation(w http.ResponseWriter, r *http.Request) {
	id := getIdFromUrls(r.URL.Path)
	for index, reservation := range reservations {
		if reservation.IdReservation == id {
			reservations = append(reservations[:index], reservations[index+1:]...)
			json.NewEncoder(w).Encode(reservations)
			return
		}
	}
	http.Error(w, "Reservation not found", http.StatusNotFound)
}

func getIdFromUrls(path string) string {
	id := path[len("/reservations/"):]
	return id
}
