def Log_Path(Filename):

    with open(Filename, "r") as LF:
        Log_Read = LF.read()

        Found = {}
        for Line in Log_Read.split( ):
            if Line in ("WARNING", "INFO", "ERROR"):
                if Line in Found:        
                    Found[Line] += 1
                else:
                    Found[Line] = 1
    return Found



def savecounts(Found,output_file):
    with open(output_file, "a") as f:    
        for result in ["ERROR", "WARNING", "INFO"]:
            f.write(f"{result} : {Found[result]}\n")
    return output_file




if __name__ == "__main__":
    # Your script logic goes here
    Found = Log_Path("New_Test.txt")
    final = savecounts(Found, "Output_log_data.txt")
    print(final)
