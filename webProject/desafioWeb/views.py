from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("""
<h1>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vel vestibulum felis, sed interdum risus. Vivamus venenatis sapien tempor, suscipit justo at, dapibus justo. Curabitur aliquet tincidunt arcu, quis aliquet lectus iaculis et. Duis ac sollicitudin arcu, feugiat convallis nisl. Vivamus cursus ligula tincidunt nunc porta bibendum. Nam arcu ex, placerat lacinia faucibus fringilla, aliquet non nibh. Maecenas luctus nunc et accumsan lacinia. Vivamus in nisi nibh. Vestibulum rhoncus aliquam velit vel mollis. Etiam in efficitur urna, et vestibulum nulla. Integer dictum lacinia mi quis efficitur. Duis iaculis, tellus a pretium tempus, dolor sapien malesuada lectus, eu lobortis erat turpis ac lectus. Praesent ultrices, massa ac dapibus faucibus, magna mauris pretium erat, at consequat nibh tellus sed eros. Sed accumsan odio purus, sed lacinia turpis pellentesque eu. Vivamus sed porta augue. Ut ac libero vitae velit dictum imperdiet nec nec turpis.
<h1/>
""")

def about(response):
    return HttpResponse("""
<h1>
    Sed suscipit condimentum massa, nec dignissim ligula sodales vel. Duis euismod faucibus turpis. Ut facilisis aliquet condimentum. Phasellus augue ipsum, viverra quis aliquet id, suscipit sit amet orci. Etiam tincidunt vitae erat vitae posuere. Praesent eget vehicula libero. Duis cursus, erat at vehicula luctus, sapien mi interdum risus, at interdum massa lacus a neque. Donec vulputate ultricies justo. Phasellus dui neque, blandit sed vehicula sed, sagittis at velit. Curabitur nec risus sollicitudin, finibus tortor in, laoreet est. Morbi vel risus neque. Aenean congue blandit lectus, eu dapibus felis accumsan vitae. Fusce id nibh porttitor, suscipit diam eu, mollis dui. Donec vel risus lorem. Nullam rutrum tempus orci, eu condimentum felis maximus a. Maecenas congue mi elit, vel tristique libero tincidunt vitae.
<h1/>
""")

def contact(response):
    return HttpResponse("""
<form method="post">
  <h1>Formulario Basico<h1/>
  <ul>
    <li>
      <label for="name">Nombre:</label>
      <input type="text" id="name" name="user_name" />
    </li>
    <li>
      <label for="mail">Correo electrónico:</label>
      <input type="email" id="mail" name="user_mail" />
    </li>
    <li>
      <label for="msg">Mensaje:</label>
      <textarea id="msg" name="user_message"></textarea>
    </li>
  </ul>
</form>
""")