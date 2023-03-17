package main

import (
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	// db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/test")
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// defer db.Close()

	// err = db.Ping()
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println("connexion reussie")
	// stmt, err := db.Prepare("INSERT INTO client(firstname, lastname, email) VALUES(?, ?, ?)")
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// defer stmt.Close()

	// res, err := stmt.Exec("Luffy", "Monckey D", "chapeaudepaille@one.piece")
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// rowsAffected, err := res.RowsAffected()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// fmt.Printf("Inserted %d rows\n", rowsAffected)

	http.HandleFunc("/clients", getClients)
	http.HandleFunc("/clients/", handleClient)
	http.HandleFunc("/reservations", getReservations)
	http.HandleFunc("/reservations/", handleReservation)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
