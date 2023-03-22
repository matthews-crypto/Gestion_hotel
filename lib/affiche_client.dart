import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

//  Classe pour stocker les informations sur les clients
class Client {
  int id;
  String nom;
  String prenom;
  String telephone;

  Client(
      {required this.id,
      required this.nom,
      required this.prenom,
      required this.telephone});

  factory Client.fromJson(Map<String, dynamic> json) {
    return Client(
        id: json['id_client'],
        nom: json['nom'],
        prenom: json['prenom'],
        telephone: json['telephone']);
  }
}

//  Fonction pour récupérer les données clients depuis l'API
Future<List<Client>> fetchClients() async {
  final response = await http.get(Uri.parse('https://api.example.com/clients'));

  if (response.statusCode == 200) {
    // 3. Décoder les données au format JSON
    List jsonResponse = json.decode(response.body);

    // 4. Stocker les informations sur les clients dans une liste
    return jsonResponse.map((client) => new Client.fromJson(client)).toList();
  } else {
    throw Exception('Failed to load clients');
  }
}

//  Créer un tableau avec les attributs "id_client", "nom", "prenom" et "telephone"
class ClientTable extends StatelessWidget {
  final List<Client> clients;

  ClientTable({required Key key, required this.clients}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return DataTable(
      columns: [
        DataColumn(label: Text('ID')),
        DataColumn(label: Text('Nom')),
        DataColumn(label: Text('Prénom')),
        DataColumn(label: Text('Téléphone'))
      ],
      rows: clients
          .map(
            (client) => DataRow(cells: [
              DataCell(Text(client.id.toString())),
              DataCell(Text(client.nom)),
              DataCell(Text(client.prenom)),
              DataCell(Text(client.telephone))
            ]),
          )
          .toList(),
    );
  }
}

// Afficher les données clients dans le tableau
class ClientScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Liste des clients"),
      ),
      body: Center(
          child: FutureBuilder<List<Client>>(
        future: fetchClients(),
        builder: (context, snapshot) {
          if (snapshot.hasError) print(snapshot.error);

          return snapshot.hasData
              ? ClientTable(
                  clients: snapshot.data,
                  key: null,
                )
              : const Center(child: CircularProgressIndicator());
        },
      )),
    );
  }
}
