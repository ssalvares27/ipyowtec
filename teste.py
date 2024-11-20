from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def carregar_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)

def abrir_com_cookies(url, cookies, nome_arquivo):
    try:
        # Configuração do Chrome
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Iniciar o driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Acessar a página de login (pode ser qualquer página da mesma sessão)
        driver.get('https://shopee.com.br')

        # Carregar cookies da sessão
        carregar_cookies(driver, cookies)

        # Agora acessar o URL do produto
        driver.get(url)

        # Esperar um tempo para a página carregar completamente
        time.sleep(5)

        # Tirar um print da tela
        driver.save_screenshot(nome_arquivo)
        print(f'Print da página salvo como: {nome_arquivo}')
        
        # Fechar o navegador
        driver.quit()
        
    except Exception as e:
        print(f'Erro ao acessar a página: {e}')

# Exemplo de uso
cookies = [
    # Aqui você deve colocar os cookies exportados do navegador
    # Exemplo:
    # {'name': 'cookie_name', 'value': 'cookie_value', 'domain': 'shopee.com.br', ...}
]
url = "https://s.shopee.com.br/3fmUr40QdC"  # URL do produto
nome_arquivo = "produto_screenshot.png"   # Nome do arquivo para salvar o print
abrir_com_cookies(url, cookies, nome_arquivo)



