package atelier1;

public class TestDe {
    public static void main(String[] args) {
        // Test Des class
        System.out.println("Testing original Des:");
        Des de = new Des(6);
        System.out.println(de.toString()); 
        de.lancerDe(5); // Roll the die 5 times

        // Test DesPipe class
        System.out.println("\nTesting DesPipe (Loaded Die):");
        DesPipe dePipe = new DesPipe(6, "Loaded Die", 4); // Minimum roll value is 4
        System.out.println(dePipe.toString()); 
        dePipe.lancerDe(5); // Roll the loaded die 5 times

        // Test DesMemory class
        System.out.println("\nTesting DesMemory (Die with Memory):");
        DesMemory deMemory = new DesMemory(6);
        System.out.println(deMemory.toString()); // Print the string representation
        for (int i = 0; i < 10; i++) {
            deMemory.lancerDe(); // Roll the die with memory 10 times
        }
    }
}

