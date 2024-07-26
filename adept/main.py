import os
import yaml
import re

def process_yml_files(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.yml'):
            input_path = os.path.join(input_dir, filename)
            
            # Read YAML content
            with open(input_path, 'r') as yml_file:
                yml_content = yaml.safe_load(yml_file)
            
            # Extract logic content
            logic_content = yml_content.get('logic', '')
            
            if logic_content:
                # Generate output filename
                output_filename = re.sub(r'^My Location_', '', filename[:-4]) + '.sql'
                output_path = os.path.join(output_dir, output_filename)
                
                # Write logic content to SQL file
                with open(output_path, 'w') as sql_file:
                    sql_file.write(logic_content.strip())
                
                print(f"Created {output_path}")
            else:
                print(f"Skipped {filename}: No logic content found")

if __name__ == "__main__":
    # Get the current working directory (should be the root of the repository in a GitHub workflow)
    repo_root = os.getcwd()
    
    # Set the correct paths relative to the repository root
    input_directory = os.path.join(repo_root, "tx", "nodes")
    output_directory = os.path.join(repo_root, "athena", "models")
    
    process_yml_files(input_directory, output_directory)