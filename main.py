import os
import sys

class EthereumAddressChecker:
  def __init__(self):
      # Path file private key
      self.private_key_file = 'privatekey.txt'
  
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
          print(f"File {self.private_key_file} tidak ditemukan!")
          return []
      except Exception as e:
          print(f"Error membaca file: {e}")
          return []
  
  def check_address(self, private_key):
      """
      Cek detail alamat dari private key
      """
      try:
          # Pastikan private key dimulai dengan '0x'
          if not private_key.startswith('0x'):
              private_key = '0x' + private_key
          
          # Proses pengecekan (contoh sederhana)
          return {
              'private_key': private_key,
              'status': 'Valid'
          }
      except Exception as e:
          return {
              'private_key': private_key,
              'error': str(e)
          }

def main():
  # Inisialisasi checker
  checker = EthereumAddressChecker()
  
  # Baca private keys
  private_keys = checker.read_private_keys()
  
  # Jika tidak ada private key
  if not private_keys:
      print("Tidak ada private key yang ditemukan!")
      sys.exit(1)
  
  # Proses setiap private key
  results = []
  for key in private_keys:
      result = checker.check_address(key)
      results.append(result)
  
  # Tampilkan hasil
  print("Hasil Pengecekan Private Key:")
  for result in results:
      print(result)

if __name__ == '__main__':
  main()
