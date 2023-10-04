package exercice1;

public class Vecteur3D {
private double x,y,z;
public Vecteur3D(double newX,double newY , double newZ) {
	this.x=newX;
	this.y=newY;
	this.z=newZ;
}
public Vecteur3D() {
	this.x=0;
	this.y=0;
	this.z=0;
}
public String toString() {
	return ("<x "+x+",y,"+y+"z>"+z);
}
public double Norme(){
	
	return Math.sqrt(x)+Math.sqrt(y)+Math.sqrt(z);
	
}
public double produitScalaire(Vecteur3D autreVecteur) {
    return x * autreVecteur.x + y * autreVecteur.y + z * autreVecteur.z;
}
public static double produitScalaire(Vecteur3D vect,Vecteur3D autreVecteur) {
    return vect.x * autreVecteur.x + vect.y * autreVecteur.y + vect.z * autreVecteur.z;
}
public Vecteur3D sommeVecteur(Vecteur3D autreVecteur) {
    double newX = this.x + autreVecteur.x;
    double newY = this.y + autreVecteur.y;
    double newZ = this.z + autreVecteur.z;
    return new Vecteur3D(newX, newY, newZ);
}
public static Vecteur3D sommeVecteur(Vecteur3D vect,Vecteur3D autreVecteur) {
    double newX = vect.x + autreVecteur.x;
    double newY = vect.y + autreVecteur.y;
    double newZ = vect.z + autreVecteur.z;
    return new Vecteur3D(newX, newY, newZ);
}
}
