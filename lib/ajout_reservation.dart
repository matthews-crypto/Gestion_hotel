// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors, library_private_types_in_public_api

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class AjoutReservation extends StatefulWidget {
  @override
  _AjoutReservationState createState() => _AjoutReservationState();
}

class _AjoutReservationState extends State<AjoutReservation> {
  final _formKey = GlobalKey<FormState>();
  final _idClientController = TextEditingController();
  final _dateReservationController = TextEditingController();
  final _nbNuitsController = TextEditingController();
  final _dateEntreController = TextEditingController();
  final _dateSortieController = TextEditingController();
  final _tarifsController = TextEditingController();

  Future<void> _submitForm() async {
    var url =
        Uri.parse('http://192.168.162.245:8080/clients/'); // L'adresse de l'API
    var idClient = _idClientController.text;
    var dateReservation = _dateReservationController.text;
    var nbNuits = _nbNuitsController.text;
    var dateEntre = _dateEntreController.text;
    var dateSortie = _dateSortieController.text;
    var tarifs = _tarifsController.text;
    var jsonData = json.encode({
      'idClient': idClient,
      'dateReservation': dateReservation,
      'nbNuits': nbNuits,
      'dateEntre': dateEntre,
      'dateSortie': dateSortie,
      'tarifs': tarifs,
    });

    var response = await http.post(url,
        body: jsonData, headers: {"Content-Type": "application/json"});

    if (response.statusCode == 200) {
      // Do something with the response
    } else {
      // Handle error
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ajouter un Réservation'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                TextFormField(
                  controller: _idClientController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    labelText: 'IdClient',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _dateReservationController,
                  keyboardType: TextInputType.datetime,
                  decoration: InputDecoration(
                    labelText: 'Date reservation',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _nbNuitsController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    labelText: 'Nombre de nuits',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _dateEntreController,
                  keyboardType: TextInputType.datetime,
                  decoration: InputDecoration(
                    labelText: 'Date entrée',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _dateSortieController,
                  keyboardType: TextInputType.datetime,
                  decoration: InputDecoration(
                    labelText: 'Date sortie',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _tarifsController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    labelText: 'Tarifs',
                  ),
                ),
                SizedBox(height: 24.0),
                ElevatedButton(
                  onPressed: _submitForm,
                  child: Text('Valider'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
