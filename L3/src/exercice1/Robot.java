package exercice1;

public class Robot {
private String refRobo ="ROB";
private String nom;
private int x,y;
private int Or;
private static int nbtotale=0;
public Robot(String nom, int x, int y, int or) {
	nbtotale++;
	this.refRobo = refRobo + nbtotale;  
	this.nom = nom;
	this.x = x;
	this.y = y;
	this.Or = or;
}
public Robot(String nom) {
	this.nom=nom;
	this.x=0;
	this.y=0;
	nbtotale++;
	this.refRobo = refRobo + nbtotale;
	this.Or=1;
}
public void modifierOr(int Or) {
	this.Or = Or;
}
public void deplacer(int Or) {
	if (Or == 1){
		this.y+=1;}
	if (Or == 2) {
		this.x+=1;
	}
	if (Or == 3){
		if (y>=1) {
		this.y-=1;
	}}
		
	if (Or == 4) {
		if (x>=1) {
		this.x-=1;
		}
	}
	}
public String toString(){
    return ("nom = "+nom+ " refRobo = "+refRobo+" x = "+x+" y = "+y+" ORIENTE = "+Or);
} 
	
}

