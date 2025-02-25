import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class BlaBlaBla {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        names.add("David");

        Iterator<String> iterator = names.iterator();
        while (iterator.hasNext()) {
            String name = iterator.next();
            if (name.startsWith("B")) {
                iterator.remove();
            }
        }

        System.out.println(names);
    }
}
