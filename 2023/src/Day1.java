import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day1 {

    void run() {
        BufferedReader reader;

        String[] numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        int s = 0;

        try {
            reader = new BufferedReader(new FileReader("data/1.data.txt"));;
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                int n1 = -1, n2 = -1;
                for (int i = 0; i < line.length(); i++) {
                    char c1 = line.charAt(i), c2 = line.charAt(line.length() - i - 1);

                    for (int j = 0; j < numbers.length; j++) {
                        if (n1 == -1 && c1 == numbers[j].charAt(0)) {
                            if (line.startsWith(numbers[j], i)) {
                                n1 = j + 1;
                            }
                        }
                        //System.out.printf("%c %c\n", c2 ,numbers[j].charAt(numbers[j].length() - 1));
                        if (n2 == -1 && c2 == numbers[j].charAt(numbers[j].length() - 1)) {
                            if (line.startsWith(numbers[j], line.length() - i - numbers[j].length())) {
                                n2 = j + 1;
                            }
                        }
                    }

                    if (n1 == -1 && Character.isDigit(c1)) {
                        n1 = Character.getNumericValue(c1);
                    }
                    if (n2 == -1 && Character.isDigit(c2)) {
                        n2 = Character.getNumericValue(c2);
                    }

                }
                //System.out.printf("%d, %d\n", n1, n2);

                s += 10 * n1 + n2;
            }
            reader.close();
        }
        catch (IOException e) {
            System.out.println(e);
        }

        System.out.println(s);
    }
}
