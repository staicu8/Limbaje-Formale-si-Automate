#include <iostream>
#include <queue>
#include <iomanip>

// Calculam densitatea cifrelor 1 și 2 în primii n termeni ai secvenței Kolakoski
// fara a stoca întreaga secvență
void densitate(long long n) {
    if (n <= 0) {
        std::cout << "Numărul de termeni trebuie să fie pozitiv" << std::endl;
        return;
    }
    else if(n==1)
    {
        std::cout<<1;
        return;
    }
else if(n==2)
{
    std::cout<<1<<" "<<2;
    return;
}
    // Initializam primii termeni
    std::queue<int> k;
    k.push(1);
    k.push(2);
    k.push(2);
    int ultim = 2;     // Retinem ultima cifra
    long long nr_total = 3; // Număr total de termeni generați
    long long nr1 = 1;  // Număr de 1
    long long nr2 = 2;// Număr de 2
    //Afisare secventa
    //std::cout<<1<<" "<<2<<" "<<2<<" ";
    k.pop();
    k.pop();
    while (nr_total < n) {
        ultim = 3 - ultim;
        // Extragem lungimea curentă a grupului
        int nr_inserare = k.front();
        k.pop();

        // Adăugăm cifre în funcție de lungimea grupului
        for (int i = 0; i < nr_inserare && nr_total < n; ++i) {
            //Pentru afisare secventa:
            //std::cout<<ultim<<" ";
            k.push(ultim);
            if (ultim == 1) {
                nr1++;
            } else {
                nr2++;
            }
            nr_total++;
        }
    }
    double density1 = static_cast<double>(nr1) / n;
    double density2 = static_cast<double>(nr2) / n;


    std::cout << "Pentru primii " << n << " termeni ai secventei Kolakoski:" << std::endl;
    std::cout << "Numărul de 1: " << nr1 << std::endl;
    std::cout << "Numărul de 2: " << nr2 << std::endl;
    std::cout << "Densitatea cifrelor de 1: " << std::fixed << std::setprecision(8) << density1 << std::endl;
    std::cout << "Densitatea cifrelor de 2: " << std::fixed << std::setprecision(8) << density2 << std::endl;
}

int main() {
    long long n;
    std::cout << "Introduceti numarul de termeni:";
    std::cin >> n;

    densitate(n);

    return 0;
}
