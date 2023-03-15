package main

import (
	"encoding/json"
	"net/http"
)

type Client struct {
	ID        string `json:"id"`
	FirstName string `json:"firstname"`
	LastName  string `json:"lastname"`
	Email     string `json:"email"`
}

var clients []Client

func getClients(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(clients)
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
	for _, client := range clients {
		if client.ID == id {
			json.NewEncoder(w).Encode(client)
			return
		}
	}
	http.Error(w, "Client not found", http.StatusNotFound)
}

func createClient(w http.ResponseWriter, r *http.Request) {
	var client Client
	err := json.NewDecoder(r.Body).Decode(&client)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	clients = append(clients, client)
	json.NewEncoder(w).Encode(client)
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
	id := getIdFromUrl(r.URL.Path)
	for index, client := range clients {

		if client.ID == id {
			clients = append(clients[:index], clients[index+1:]...)
			json.NewEncoder(w).Encode(clients)
			return
		}
	}
	http.Error(w, "Client not found", http.StatusNotFound)
}

func getIdFromUrl(path string) string {
	id := path[len("/clients/"):]
	return id
}
