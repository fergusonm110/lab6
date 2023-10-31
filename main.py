#Mariah Ferguson
password = ''
#encodes password
def encode(password):
  password = input()
  encoder = list(password)
  for i in range(0, len(encoder)):
    # if encoder[i] + 3 is greater than 9
    if encoder[i] == '7':
      encoder[i] = '0'
    elif  encoder[i] == '8':
      encoder[i] = '1'
    elif  encoder[i] == '9':
     encoder[i] = '2'
    else:
      #adds three to each value
      encoder[i] = int(encoder[i])
      encoder[i] = str(encoder[i] + 3)
  encodepass = ''.join(encoder)
  return encodepass
def main():
  
  #displays menu
  def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit") 
    
  while True:
    menu()
    print("Please enter an option:")
    menuselect = int(input())
    if menuselect == 1:
      print("Please enter your password to encode: ")
      encode(password)
      print("Your password has been encoded and stored!\n")
    if menuselect == 3:
      break
if __name__=='__main__': main()
  
