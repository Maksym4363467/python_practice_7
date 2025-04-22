from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import print_to_console, write_to_file_builtin


def main():
    console_text = read_from_console()
    print_to_console(f"[З консолі]: {console_text}")
    write_to_file_builtin("output_console.txt", console_text)

    file_text = read_from_file_builtin("sample.txt")
    print_to_console(f"[З файлу]: {file_text}")
    write_to_file_builtin("output_file.txt", file_text)

    df = read_from_file_pandas("sample.csv")
    df_str = df.to_string(index=False)
    print_to_console(f"[З CSV]:\n{df_str}")
    write_to_file_builtin("output_pandas.txt", df_str)

if __name__ == "__main__":
    main()