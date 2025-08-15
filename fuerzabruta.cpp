#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <limits>
using namespace std;

// 1. Coordenadas mas cercanas 
vector<pair<double, double>> Coordenadas = {
    {-2.423, -8.469},
    {5.721, 9.354},
    {6.766, -3.823},
    {4.129, 6.744},
    {5.371, -5.404}
};

pair<double, double> findclosest(double x, double y){
    pair<double, double> closest = Coordenadas[0];
    double min_dist = numeric_limits<double>::max();

    for (const auto& coord : Coordenadas) {
        double dist = sqrt(pow(coord.first - x, 2) + pow(coord.second - y, 2));
        if (dist < min_dist) {
            min_dist = dist;
            closest = coord;
        }
    }
    return closest;
}

int main() {
    pair<double, double> result = findclosest(0, 0); // Cambia las coordenadas según sea necesario
    cout << "Puntos más cercanos: (" << result.first << ", " << result.second << ")" << endl;
    //Imprimir distancia entre los puntos mas cercanos
    double dist = sqrt(pow(result.first - 1, 2) + pow(result.second - 1, 2));
    cout << "Distancia: " << dist << endl;
    return 0;
}


//2. String matching 
