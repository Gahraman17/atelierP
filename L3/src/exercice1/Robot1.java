package exercice1;

public class Robot1 {
private String refR = "ROB";
private String nom;
private int x,y;
private int Ort;
private static int nbtotale = 0;
public Robot1(String nom, int x, int y, int ort) {
	this.Ort = ort ;
	this.nom = nom;
	this.x = x;
	this.y = y;
	nbtotale++;
	this.refR = refR + nbtotale;  
}
public Robot1 (String nom) {
	this.nom =nom;
	this.x=0;
	this.y=0;
	this.Ort = 1;
	nbtotale++;
	this.refR = refR + nbtotale;  
}
public void modifierOr(int or) {
	this.Ort = or;
}
public String toString() {
	return ("nom "+this.nom+" refR "+this.refR+" x,y "+x+","+y+" ort "+this.Ort);
}
}
