import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        unique_integers = set()
        
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                # Strip leading/trailing whitespace and split the line
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split()
                if len(parts) != 1:
                    continue
                
                try:
                    number = int(parts[0])
                    unique_integers.add(number)
                except ValueError:
                    continue
        
        # Write the sorted unique integers to the output file
        with open(output_file_path, 'w') as output_file:
            for number in sorted(unique_integers):
                output_file.write("{}\n".format(number))

def main():
    input_folder = "/dsa/hw01/sample_inputs/"
    output_folder = "/dsa/hw01/sample_results/"
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each input file in the sample_inputs folder
    for input_file_name in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, input_file_name)
        output_file_name = "{}_results.txt".format(input_file_name)
        output_file_path = os.path.join(output_folder, output_file_name)
        
        UniqueInt.process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
