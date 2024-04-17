
# api/views.py
import base64
from django.shortcuts import render

def index(request):
    return render(request, 'home.html') 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('admin_signup')
        else:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('admin_login')
            except:
                messages.error(request, 'Error creating account. Please try again.')
                return redirect('admin_signup')

    return render(request, 'admin_signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('user_signup')

        try:
            user1 = User.objects.create_user(username=username, password=password1)
            user1.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('user_login')
        except:
            messages.error(request, 'Error creating account. Please try again.')
            return redirect('user_signup')

    return render(request, 'user_signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user1 = authenticate(request, username=username, password=password)

        if user1 is not None:
            login(request, user1)
            messages.success(request, 'Login successful.')
            return redirect('user_page')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('user_login')

    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home page or another page

from django.shortcuts import render




import qrcode
from django.http import HttpResponse, JsonResponse
from PIL import Image

from django.http import JsonResponse


#def verify_qr_code(request):
#    if request.method == 'POST':
#       qr_code_hash = request.POST.get('qr_code_hash', '')
#       # Perform verification logic here, such as checking the hash against a database
#       # For demonstration purposes, we'll just return a success response if the hash is not empty
 #       if qr_code_hash:
  #          return JsonResponse({'message': 'QR code verified successfully.'})
   #     else:
    #        return JsonResponse({'message': 'QR code verification failed.'}, status=400)
  #  else:
   #     return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405) 

from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import io

from pyzbar.pyzbar import decode
from django.shortcuts import render

#def add_product_view(request):
  #  if request.method == 'POST':
   #    product_address = request.POST.get('product_address')
    #    product_name = request.POST.get('product_name')
#
        # Call the add_product function from Blockchain.py
 #       tx_receipt = add_product(product_address, product_name)
#
        # Check transaction receipt for success or failure
 #       if tx_receipt.status:
            # Transaction successful
  #          return render(request, 'admin_page.html')
   #     else:
            # Transaction failed
    #        return render(request, 'admin_page.html')

  #  return render(request, 'admin_page.html')

def verify_qr_code(request):
    return render(request, 'user_page.html')

def verify_qr_code_process(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data', '')
        image_data = image_data.replace('data:image/jpeg;base64,', '')
        image_data = image_data.replace('data:image/png;base64,', '')
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        qr_code_data = decode(image)
        if qr_code_data:
            # Assuming qr_code_data is a list of decoded QR codes
            qr_code_content = qr_code_data[0].data.decode('utf-8')
            # Implement your verification logic here
            if verify_qr_code_content(qr_code_content):
                return JsonResponse({'message': 'QR code verified successfully'})
            else:
                return JsonResponse({'message': 'QR code verification failed'})
    return JsonResponse({'message': 'Invalid request'})

def verify_qr_code_content(qr_code_content):
    # Implement your verification logic here
    # For example, compare the content with a database of valid QR codes
    valid_qr_codes = ['qr_code_1', 'qr_code_2', 'qr_code_3']
    if qr_code_content in valid_qr_codes:
        return True
    return False

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def admin_login_submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            # Redirect to the admin page
            return redirect('admin_page')
        else:
            # Invalid login
            return render(request, 'admin_login.html', {'error_message': 'Invalid username or password'})
    else:
        return redirect('admin_login')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def admin_signup_submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'admin_signup.html', {'error_message': 'Username already taken'})

        # Create the new admin user
        user = User.objects.create_user(username=username, password=password)
        user.is_staff = True  # Make the user a staff member (admin)
        user.save()

        # Redirect to the admin login page
        return redirect('admin_login')
    else:
        return redirect('admin_signup')
    
import qrcode
from django.conf import settings
import os
import qrcode
from django.conf import settings



from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

from django.http import JsonResponse

from django.http import JsonResponse

from django.http import JsonResponse

import qrcode

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user1 = authenticate(request, username=username, password=password)

        if user1 is not None:
            login(request, user1)
            messages.success(request, 'Login successful.')
            return redirect('admin_page')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('admin_login')

    return render(request, 'admin_login.html')


def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('admin_signup')

        try:
            user1 = User.objects.create_user(username=username, password=password1)
            user1.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('admin_login')
        except:
            messages.error(request, 'Error creating account. Please try again.')
            return redirect('admin_signup')

    return render(request, 'admin_signup.html')




# views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
import hashlib

def generate_hash(name, brand, price, manufacturer_id, product_sn):
    data = f"{name}{brand}{price}{manufacturer_id}{product_sn}".encode('utf-8')
    hash_code = hashlib.sha256(data).hexdigest()
    return hash_code

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import hashlib
import qrcode


import hashlib
import os
import qrcode
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product

def generate_qr_code(product_sn):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(product_sn)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def admin_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        manufacturer_id = request.POST.get('manufacturer_id')
        product_sn = request.POST.get('product_sn')
        
        # Generate a hash code for the product
        hash_code = hashlib.md5(product_sn.encode()).hexdigest()
        
        # Save the product to the database
        product = Product(name=name, brand=brand, price=price, manufacturer_id=manufacturer_id, product_sn=product_sn)
        product.save()
        
        # Generate and save QR code image
        qr_code = generate_qr_code(product_sn)
        qr_code_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', f'{product_sn}.png')
        qr_code.save(qr_code_path)
        
        return JsonResponse({'success': True, 'hash_code': hash_code, 'name': name, 'brand': brand, 'price': price, 'qr_code_url': qr_code_path})
    else:
        return render(request, 'admin_page.html')

import qrcode
from django.http import JsonResponse
from PIL import Image
import hashlib



import qrcode
from django.http import JsonResponse
from PIL import Image
import hashlib

import qrcode
from django.http import JsonResponse
from PIL import Image
import hashlib

import qrcode
from django.http import JsonResponse
from PIL import Image
import hashlib

def generate_hash(product_sn):
    return hashlib.md5(product_sn.encode()).hexdigest()

import qrcode
from django.http import JsonResponse
from PIL import Image
import hashlib
from .models import Product

import qrcode
import hashlib
import os

import qrcode
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .blockchain_service import contract
from .blockchain_service import w3

def generate_qr_code(hash_code, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(hash_code)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

from django.http import JsonResponse

from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.contrib import messages

def register_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            brand = form.cleaned_data['brand']
            price = int(form.cleaned_data['price'])  # Convert to uint256
            manufacturer_id = form.cleaned_data['manufacturer_id']
            product_sn = int(form.cleaned_data['product_sn'])  # Convert to uint256
            
            # Check if product with the same serial number already exists
            if Product.objects.filter(product_sn=product_sn).exists():
                messages.error(request, 'Product with the same serial number already registered.')
                return render(request, 'admin_page.html', {'form': form})
            
            # Save the product to the database
            product = Product.objects.create(name=name, brand=brand, price=price, manufacturer_id=manufacturer_id, product_sn=product_sn)

            # Generate hash code for product registration (using blockchain transaction hash)
            tx_hash = contract.functions.registerProduct(name, brand, price, manufacturer_id, product_sn).transact({'from':'0xAA8cCA214D7D0B21BE1e9A483671eca823B0eE2F' })
            try:
                # Wait for transaction receipt
                tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            except TimeoutError:
                # Handle timeout error
                return render(request, 'registration_failed.html')

            # Get transaction hash
            hash_code = tx_receipt.transactionHash.hex()
            # Update the product with the hash code
            product.hash_code = hash_code
            product.save()

            # Specify the file path where the QR code will be saved
            file_path = f'C:/Users/user/Desktop/Blockchain_Project/fake_product_identification/qrcodes/{name}_{product_sn}_qr_code.png'

            # Generate and save the QR code
           
            generate_qr_code(hash_code, file_path)
            return render(request, 'registration_success.html', {'tx_hash': tx_hash, 'hash_code': hash_code})
    else:
        form = ProductForm()
    
    return render(request, 'admin_page.html', {'form': form})



import hashlib
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from pyzbar.pyzbar import decode
from PIL import Image
import io

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product



from django.shortcuts import render, redirect
from .models import Product
import hashlib


def verify_product(request):
    if request.method == 'POST':
        hash_code = request.POST.get('hash_code')
        try:
            product = Product.objects.get(hash_code=hash_code)
            # Check if the hash code corresponds to a valid blockchain transaction
            tx_hash = product.hash_code
            if w3.eth.get_transaction_receipt(tx_hash) is not None:
                # Assuming the verification is successful, you can redirect to the product information page
                return redirect('product_info_page', name=product.name, brand=product.brand, price=product.price, manufacturer_id=product.manufacturer_id, product_sn=product.product_sn)
            else:
                return render(request, 'invalid_hash.html')
        except Product.DoesNotExist:
            return render(request, 'invalid_hash.html')
    else:
        return render(request, 'user_page.html')


from django.shortcuts import render

from django.shortcuts import render
from .models import Product

def product_info_page(request, name, brand, price, manufacturer_id, product_sn):
    # Assuming Product is your model
    product = Product.objects.get(name=name, brand=brand, price=price, manufacturer_id=manufacturer_id, product_sn=product_sn)
    return render(request, 'product_info.html', {'product': product})

from django.shortcuts import render, redirect
from .models import Product

def delete_products(request):
    if request.method == 'POST':
        product_ids = request.POST.getlist('products')
        Product.objects.filter(id__in=product_ids).delete()
        return redirect('product_list')  # Redirect to a page displaying the updated list of products
    else:
        products = Product.objects.all()
        return render(request, 'delete_products.html', {'products': products}) 
