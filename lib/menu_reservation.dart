import 'package:flutter/material.dart';
import 'package:la_corniche/ajout_reservation.dart';
// ignore_for_file: prefer_const_constructors, use_key_in_widget_constructors, file_names, sort_child_properties_last

class MenuReservation extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Gestion Réservation'),
        centerTitle: true,
        backgroundColor: Colors.deepPurple.shade300,
      ),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('images/background3.jpg'),
            fit: BoxFit.cover,
          ),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => AjoutReservation()),
                  );
                },
                child: Text('Ajout Reservation'),
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  minimumSize: Size(200, 60),
                  backgroundColor: Colors.cyan.withOpacity(0.5),
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {},
                child: Text('Affichage Réservation'),
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  minimumSize: Size(200, 60),
                  backgroundColor: Colors.cyan.withOpacity(0.5),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
