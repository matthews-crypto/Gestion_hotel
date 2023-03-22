// ignore_for_file: prefer_const_constructors, use_key_in_widget_constructors, file_names, sort_child_properties_last

import 'package:flutter/material.dart';
import 'package:la_corniche/menu_client.dart';
import 'package:la_corniche/menu_reservation.dart';

class MenuSection extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Menu de Gestion'),
        centerTitle: true,
      ),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('images/background.jpg'),
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
                    MaterialPageRoute(builder: (context) => MenuClient()),
                  );
                },
                child: Text('Gestion clients'),
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  minimumSize: Size(200, 60),
                  backgroundColor: Colors.deepPurpleAccent.withOpacity(0.8),
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => MenuReservation()),
                  );
                },
                child: Text('Gestion réservations'),
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  minimumSize: Size(200, 60),
                  backgroundColor: Colors.deepPurpleAccent.withOpacity(0.8),
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {},
                child: Text('Gestion factures'),
                style: ElevatedButton.styleFrom(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  minimumSize: Size(200, 60),
                  backgroundColor: Colors.deepOrange.withOpacity(0.6),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
