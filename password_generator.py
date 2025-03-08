import string
import random
# facebook : CQ-.6Kg7Yv(<y%O , yahoo : &@)oWk+9#JnO0T[
def generate() -> str :
    strs = [string.ascii_letters + string.digits + string.punctuation]
    sampled = random.sample(strs[0], k=15)
    note = input('- Generate Password Is For : ').capitalize()
    print(f'- {note} Password : ' , end='')
    for password in sampled:
        print(*password, end='')
        
    
if __name__ == '__main__':
    generate()



