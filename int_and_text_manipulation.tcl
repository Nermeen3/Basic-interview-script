set char_c 0; set even_c 0; set odd_c 0; set invalid_c 0;
set special_chars "!#$%&*+,-./:;<=>?@\^~"
set sum2int 0; set concat3str ""; set index 0;
set filename "input.txt"
set file_ [open $filename r]

puts "------------------- integers and strings manipulations:------------------\n"
while {[gets $file_ data] >= 0} {
    set first [string index $data 0];

    # true if first element in string isnt empty
    if {$first ne ""} {
        if {$char_c == 0} {set min_str [string length $data]}; # initializing min string length
        if {[string first $first $special_chars] != -1} {set char_c [expr "$char_c + 1"]; # checking for special char
        puts "$data";
        if {$char_c <= 3} {append concat3str $data; append concat3str " "}
    } else {if {[regexp {^[0-9]+|[a-zA-Z]+} $data ]} {
        regsub -all {(\d+\.+\d+)} $data "" output; # eliminating all floats using regular expression and save them in "output"
        set numbers [regexp -all -inline -- {[0-9]+} $output]; # returns all integers using regexp
        set e 0; set o 0;
        foreach int $numbers {
            if {$even_c + $odd_c == 0} {set max_int $int}; # initialize max int
            if {$int%2 != 0} {set result [expr "$int / 2"]; puts "$int is odd and result is: $result"; incr o} else {
                set result [expr "$int * 3.25"]; puts "$int is even and result is: $result"; incr e}
            if {$int > $max_int} {set max_int $int;};  # finding max int in file
            if {$index < 2} {incr sum2int $int; incr index}; # sum of first two ints
            };
        if {$e > 0} {incr even_c}; # incrementing only 1 for each line that has even or odd
        if {$o > 0} {incr odd_c};  
        }
    }
    if {$min_str > [string length $data]} {set min_str [string length $data]}; # min length of non empty string
    } else {puts "INVALID LINE"; incr invalid_c;}
}
close $file_

puts "----------------------- END OF FILE -----------------------\n"
puts "Number of lines containing string  :  $char_c";
puts "Number of lines containing even    :  $even_c";
puts "Number of lines containing odd     :  $odd_c";
puts "Number of lines containing invalid :  $invalid_c\n";

puts "Summation of the first two integers:   $sum2int";
puts "Concat. of the first 3 special strings:$concat3str";
puts "maximum integer found in the file: $max_int";
puts "minimum length of non empty string: $min_str";

# I implemented the lengths along with each line after manipulations in the python code since it's a more efficient way
puts "------------------------\nlines with their lengths"
set file_ [open $filename r]
while {[gets $file_ data] >= 0} {
    puts "$data [string length $data]"}
close $file_








 