package exercice1;

public class TestVecteur3D {
public static void main(String [] args) {
	Vecteur3D v = new Vecteur3D(1,2,3);
	Vecteur3D w = new Vecteur3D(10,12,53);
	Vecteur3D o = new Vecteur3D(81,32,13);
	System.out.println(v);
	System.out.println("nord de v est = "+v.Norme());
	System.out.println(w);
	System.out.println("nord de w est = "+w.Norme());
	System.out.println(o);
	System.out.println("nord de o est = "+o.Norme());
	System.out.println("v + w "+Vecteur3D.sommeVecteur(v,w));
}
}
