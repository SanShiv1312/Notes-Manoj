def remove_duplicate(files):
    # Accessing each element to compare with two loops
    for i in files:
        # In second loop check the `i`  file with another file in directory
        for j in files:
            # Ignoring same file to be checked again
            if i != j:
                # Opening the files to read with binary
                file1 = open(i,'rb')
                file2 = open(j,'rb')
                # Checking the same data is there in two files
                # If so removing it from directory
                if (file1.read() == file2.read()):
                    print("Same file detected", i, j)
                    os.system("rm "+i)
                    # Upating the files variable
                    files = os.listdir()
                    break

if __name__ == '__main__':
    files = os.listdir()
    print('Are you sure to remove the duplicate files')
    print('Press enter or pass any value to confirm')
    print('If you don\'t want to remove duplicates, press Ctrl+C')
    try:
        input("\n>>>")
    except KeyboardInterrupt:
        print("\b\b  ")
        print("Exited safely! 😉")
        exit()
    remove_duplicate(files)
