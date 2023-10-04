package atelier1;

public class Entier {
protected int valeur;
protected int valeurMax;
protected int valeurMin;

public Entier(int valeurMI,int valeurMA) {
	this.valeurMax = valeurMI;
	this.valeurMin = valeurMA;
	this.valeur = 0;
}
public Entier() {
	this.valeur = 0;
}
public void setValeur(int valeur) {
	if(valeur >= valeurMin && valeur <= valeurMax) {
	    this.valeur = valeur;
}
	else {
		System.out.println("La valeur n'est pas dans les bornes spécifiées.");
	}
	
}
public int getEntier() {
    return this.valeur;
}
public void increment() {
    if (this.valeur + 1 <= this.valeurMax) {
        this.valeur += 1;
    }
}

public void increment(int n) {
    if (this.valeur + n <= this.valeurMax) {
        this.valeur += n;
    }
}

public String toString() {
	return ("la valeur est :"+this.valeur);
}
@Override
public boolean equals(Object obj) {
    if (this == obj) {
        return true;
    }

    if (obj instanceof Entier) {
        Entier other = (Entier) obj;
        return this.valeur == other.valeur;
    }

    return false;
}
}
