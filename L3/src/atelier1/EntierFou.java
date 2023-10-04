package atelier1;

import java.util.Random;

public class EntierFou extends Entier{
	
protected int niveauDeFoulie;
protected int valeur;
protected static Random r = new Random();

public EntierFou(int valeur , int niveauDeFou,int valeurMin,int valeurMax) {
	
	super(valeurMin,valeurMax);
	this.valeur = valeur;
	this.niveauDeFoulie = niveauDeFou;
	
}

public void increment(int n) {
	int nb = r.nextInt(n);  
	 if (this.valeur + nb <= this.valeurMax) {
	        this.valeur += nb;
	    }
}

}
