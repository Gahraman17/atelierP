package atelier1;

public class DesPipe extends Des {
    private final int minRoll;

    public DesPipe(int nbFaces, String nom, int minRoll) {
        super(nbFaces, nom);
        if (minRoll >= 1 && minRoll <= nbFaces) {
            this.minRoll = minRoll;
        } else {
        	System.err.println("Valeur de lancement minimale invalide. Réglage de minRoll sur une valeur par défaut.");
            this.minRoll = 1; // Set to the minimum possible value as an example.
        }
    }
    @Override
    public void lancerDe() {
        int nbAleatoire = r.nextInt(this.nbFaces - minRoll + 1) + minRoll; // Ensure a roll >= minRoll
        System.out.println(nbAleatoire);
    }
}
