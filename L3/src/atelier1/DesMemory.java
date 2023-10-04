package atelier1;

public class DesMemory extends Des {
    private int previousRoll ;

    public DesMemory(int nbFaces) {
        super(nbFaces);
    }

    @Override
    public void lancerDe() {
        int currentRoll;
        do {
            currentRoll = super.lancerDe(1); // Roll once
        } while (currentRoll == previousRoll); // Repeter until it's different

        previousRoll = currentRoll; // Update roll
    }
}

