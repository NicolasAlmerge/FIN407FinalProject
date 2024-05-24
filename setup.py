import gdown
import os


__all__ = ()


def print_warning(text: str, /):
    print("\033[93m❗️ WARNING: " + text + "\033[0m")


def print_success(text: str, /):
    print("\033[92m✅ SUCCESS: " + text + "\033[0m")


def print_error(text: str, /):
    print("\033[91m❌ ERROR: " + text + "\033[0m")


def print_info(text: str, /):
    print("\033[94m👉 INFO: " + text + "\033[0m")


def ask_confirmation(prompt: str, /) -> bool:
    x = input(prompt + " [y/n] ").strip().lower()
    if x in ("y", "yes"):
        return True
    if x in ("n", "no"):
        return False
    print_error("Invalid answer: should be 'yes', 'y', 'no' or 'n'.")
    exit(1)


def create_env_file():
    if os.path.isfile(".env"):
        if not ask_confirmation("'.env' file already exists, do you want to overwrite it?"):
            return
    wrds_username = input("Enter your WRDS username: ").strip()
    if not wrds_username:
        print_warning("No WRDS username was given, running some cells might fail.")
    with open(".env", "w") as f:
        f.write("WRDS_USERNAME="+wrds_username)
    print_success("Successfully created '.env' file!")


def download_file_from_google_drive(id: str, output_file_name: str, /):
    gdown.download("https://drive.google.com/uc?id="+id, os.path.join("data", output_file_name))


def install_all_required_files():
    print_info("Downloading files from Google Drive...")
    download_file_from_google_drive("1KjGhSE1XBuHqVNbBsdSabKM2HZsy66Ym", "signed_predictors_all_wide.csv")
    download_file_from_google_drive("1AyjvUWg5QTFtfd09mGh6Sb3unDnfACP6", "1_3_all_returns_values.csv")
    print_success("Successfully downloaded all files from Google Drive!")


def setup_main():
    create_env_file()
    install_all_required_files()


if __name__ == "__main__":
    setup_main()
