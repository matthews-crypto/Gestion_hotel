// ignore_for_file: use_key_in_widget_constructors, library_private_types_in_public_api, prefer_const_constructors, unused_import, unused_local_variable

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class AjoutClient extends StatefulWidget {
  @override
  _AjoutClientState createState() => _AjoutClientState();
}

class _AjoutClientState extends State<AjoutClient> {
  final _formKey = GlobalKey<FormState>();
  final _nomController = TextEditingController();
  final _prenomController = TextEditingController();
  final _telephoneController = TextEditingController();

  Future<void> _submitForm() async {
    var url = Uri.parse(
        'http://192.168.162.245:8080/clients/'); // Remplacer par l'adresse de l'API
    var nom = _nomController.text;
    var prenom = _prenomController.text;
    var telephone = _telephoneController.text;
    var jsonData =
        json.encode({'nom': nom, 'prenom': prenom, 'telephone': telephone});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ajouter un client'),
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
                  controller: _nomController,
                  decoration: InputDecoration(
                    labelText: 'Nom',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _prenomController,
                  decoration: InputDecoration(
                    labelText: 'Prénom',
                  ),
                ),
                SizedBox(height: 12.0),
                TextFormField(
                  controller: _telephoneController,
                  decoration: InputDecoration(
                    labelText: 'Téléphone',
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
