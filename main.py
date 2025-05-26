import os
import sys
import logging
from datetime import datetime
from eth_account import Account

class EthereumAddressChecker:
  def __init__(self):
      # Path file private key
      self.private_key_file = 'privatekey.txt'
      
      # Siapkan logging
      self.setup_logging()
  
  def setup_logging(self):
      """
      Konfigurasi logging
      """
      # Buat direktori logs jika belum ada
      os.makedirs('logs', exist_ok=True)
      
      # Nama file log dengan timestamp
      log_filename = f'logs/ethereum_addresses_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
      
      # Konfigurasi logging
      logging.basicConfig(
          level=logging.INFO,
          format='%(message)s',
          handlers=[
              logging.FileHandler(log_filename),
              logging.StreamHandler(sys.stdout)
          ]
      )
      self.logger = logging.getLogger(__name__)
  
  def read_private_keys(self):
      """
      Baca private key dari file
      """
      try:
          with open(self.private_key_file, 'r') as file:
              # Baca semua baris, hapus whitespace
              keys = [key.strip() for key in file.readlines() if key.strip()]
          return keys
      except FileNotFoundError:
          self.logger.error(f"File {self.private_key_file} tidak ditemukan!")
          return []
      except Exception as e:
          self.logger.error(f"Error membaca file: {e}")
          return []
  
  def get_address_from_private_key(self, private_key):
      """
      Dapatkan alamat Ethereum dari private key
      """
      try:
          # Pastikan private key dimulai dengan '0x'
          if not private_key.startswith('0x'):
              private_key = '0x' + private_key
          
          # Buat akun dari private key
          account = Account.from_key(private_key)
          
          # Kembalikan alamat
          return account.address
      except Exception as e:
          self.logger.error(f"Error mengonversi private key: {e}")
          return None

def main():
  # Inisialisasi checker
  checker = EthereumAddressChecker()
  
  # Baca private keys
  private_keys = checker.read_private_keys()
  
  # Jika tidak ada private key
  if not private_keys:
      checker.logger.error("Tidak ada private key yang ditemukan!")
      sys.exit(1)
  
  # Proses setiap private key
  addresses = []
  for key in private_keys:
      address = checker.get_address_from_private_key(key)
      if address:
          addresses.append(address)
          checker.logger.info(address)  # Log setiap alamat
  
  # Log total alamat
  checker.logger.info(f"\nTotal alamat: {len(addresses)}")

if __name__ == '__main__':
  main()
