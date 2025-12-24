import os
import subprocess

class Anbernic:
    
    def __init__(self):
        uname_output = subprocess.check_output(["uname", "-a"], text=True).strip()
        print("System uname output:", uname_output)

        # If CFW knulli, custom path, else, stock path
        if "knulli" in uname_output.lower():
            self.__sd1_rom_storage_path = "/userdata/roms"
            self.__sd2_rom_storage_path = "/userdata/roms"
            self.__rom_folder_mapping = {
                "PSP": "psp",
                "PS": "psx",
                "GBA": "gba",
                "GBC": "gbc",
                "GB": "gb",
                "NDS": "nds",
                "N64": "n64",
                "FC": "nes",
                "SFC": "snes",
                "MD": "megadrive",
                "SMS": "mastersystem",
                "GG": "gamegear",
                "SEGA32X": "sega32x",
            }
        else:
            self.__sd1_rom_storage_path = "/mnt/mmc/Roms"
            self.__sd2_rom_storage_path = "/mnt/sdcard/Roms"

            self.__rom_folder_mapping = {
                "PSP": "PSP",
                "PS": "PS",
                "GBA": "GBA",
                "GBC": "GBC",
                "GB": "GB",
                "NDS": "NDS",
                "N64": "N64",
                "FC": "FC",
                "SFC": "SFC",
                "MD": "MD",
                "SMS": "SMS",
                "GG": "GG",
                "SEGA32X": "SEGA32X",
            }
        self.__current_sd = 2

    def get_sd1_storage_path(self):
        return self.__sd1_rom_storage_path

    def get_sd2_storage_path(self):
        return self.__sd1_rom_storage_path
    
    def get_sd1_storage_console_path(self, console):
        return os.path.join(self.__sd1_rom_storage_path, self.__rom_folder_mapping[console])

    def get_sd2_storage_console_path(self, console):
        return os.path.join(self.__sd2_rom_storage_path, self.__rom_folder_mapping[console])
    
    def set_sd_storage(self, sd):
        if sd == 1 or sd == 2:
            self.__current_sd = sd
    
    def get_sd_storage(self):
        return self.__current_sd
    
    def switch_sd_storage(self):
        if self.__current_sd == 1:
            self.__current_sd = 2
        else:
            self.__current_sd = 1
    
    def get_sd_storage_path(self):
        if self.__current_sd == 1:
            return self.get_sd1_storage_path()
        else:
            return self.get_sd2_storage_path()
    
    def get_sd_storage_console_path(self, console):
        if self.__current_sd == 1:
            return self.get_sd1_storage_console_path(console)
        else:
            return self.get_sd2_storage_console_path(console)
    
# "NEOGEO"
# "VARCADE"
# "CPS1"
# "CPS2"
# "CPS3"
# "FBNEO"
# "MAME"
# "FC"
# "SFC"
# "SMS"
# "MD"
# "SEGA32X"
# "PCE"
# "NGP"
# "GG"
# "WS"
# "OPENBOR"
# "DREAMCAST"
# "A800"
# "A2600"
# "A5200"
# "A7800"
# "AMIGA"
# "ATARIST"
# "ATOMISWAVE"
# "C64"
# "DOS"
# "EASYRPG"
# "FDS"
# "GW"
# "HBMAME"
# "LYNX"
# "MDCD"
# "MSX"
# "NAOMI"
# "NEOCD"
# "ONS"
# "PCECD"
# "PGM2"
# "PICO"
# "POKE"
# "SATURN"
# "SCUMMVM"
# "VB"
# "VIC20"
# "PORTS"
