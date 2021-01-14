# Constants

# General constants for packet parsing
ETHII_HEADER = 14     # Bytes used for header in ETHII protocol (OSI-Layer 1)
IPV4_HEADER = 20      # Bytes used for header in IPV4 protocol (OSI-Layer 2)
UDP_HEADER = 8        # Bytes used for header in UDP protocol (OSI-Layer 2)

# CODIF constants
CODIF_HEADER = 64
CODIF_PAYLOAD = 7168
CODIF_BLOCKS_IN_PACKET = 128
CODIF_CHANNELS_IN_BLOCK = 7
CODIF_POLARIZATION = 2
CODIF_HEADER_TOTAL = ETHII_HEADER + IPV4_HEADER + UDP_HEADER + CODIF_HEADER
CODIF_PACKET_SIZE = CODIF_PAYLOAD + CODIF_HEADER
CODIF_TOTAL_SIZE = CODIF_HEADER_TOTAL + CODIF_PAYLOAD
PAF_EPOCH_PERIOD = 250000
PAF_SAMPLE_PERIOD = (1e6*32/27)

DADA_HEADER_SIZE = 4096
PAF_N_FREQ_GROUP = 48
ODC_PORT = 191
N_PAF_PORTS = 188
N_ELEMENTS = 192
PAF_BANDWIDTH = (1+CODIF_CHANNELS_IN_BLOCK)*PAF_N_FREQ_GROUP

# List of used elements during snapshot observation from 07.12.20 and 09.12.20
ELEMENT_LIST = [15,16,18,19,25,26,27,28,29,30,35,36,37,38,39,40,45,46,47,48,49,50,55,56,57,58,59,60,65,67,68,69,70,77,76,80,
    159,158,129,119,169,150,149,139,120,110,161,160,141,140,130,111,162,152,151,132,131,121,172,153,143,142,123,122,173,144,134,133,114,154,164,124]
