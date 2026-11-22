<p align="center">
  <img src="https://raw.githubusercontent.com/diegofonterosa/diegofonterosa/main/assets/banner_cyberpunk.png" alt="Banner Diego Pérez Fonterosa" />
</p>

<h1 align="center">Hola, soy Diego Pérez Fonterosa</h1>
<h3 align="center">Sistemas y ciberseguridad · SOC · NOC · Soporte IT</h3>

<p align="center">
  <a href="https://portfoliodiegofonterosa.netlify.app"><img src="https://img.shields.io/badge/Portfolio-00ff41?style=for-the-badge&logo=netlify&logoColor=black" alt="Portfolio" /></a>
  <img src="https://img.shields.io/badge/Disponible-desde%2016%2F12%2F2026-00d4ff?style=for-the-badge" alt="Disponible desde el 16/12/2026" />
  <img src="https://komarev.com/ghpvc/?username=diegofonterosa&style=for-the-badge&color=blueviolet" alt="Visitas del perfil" />
</p>

## Sobre mí

Durante **16 años** trabajé como operador técnico en una **central receptora de alarmas**: monitorización 24/7, gestión de incidencias en tiempo real y soporte técnico. Ahora llevo esa experiencia a la seguridad informática.

- Terminando el **CFGS de ASIR** (nota media 9,06) y el **Máster en Ciberseguridad**
- Prácticas como **técnico de sistemas** en una empresa de Vigo: auditoría de Active Directory, VPN, soporte a usuarios y Helpdesk
- **Laboratorio propio**: Wazuh, TheHive, Cortex, n8n, honeypot Cowrie y entorno de pentest con Kali
- Busco puesto de **SOC N1, NOC, monitorización o soporte N1/N2**, en remoto o en la zona de Vigo

## Stack tecnológico

<p align="center">
  <img src="https://img.shields.io/badge/Wazuh-005571?style=flat-square" alt="Wazuh" />
  <img src="https://img.shields.io/badge/TheHive-F3B700?style=flat-square&logoColor=black" alt="TheHive" />
  <img src="https://img.shields.io/badge/Cortex-4B5563?style=flat-square" alt="Cortex" />
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="n8n" />
  <img src="https://img.shields.io/badge/MITRE_ATT%26CK-C8102E?style=flat-square" alt="MITRE ATT&CK" />
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Metasploit-2596CD?style=flat-square" alt="Metasploit" />
  <img src="https://img.shields.io/badge/OpenVAS-66C430?style=flat-square" alt="OpenVAS" />
  <img src="https://img.shields.io/badge/Active_Directory-0078D4?style=flat-square&logo=windows&logoColor=white" alt="Active Directory" />
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="40" alt="Linux" title="Linux" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python" title="Python" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="40" alt="Bash" title="Bash" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="40" alt="Docker" title="Docker" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" height="40" alt="Node.js" title="Node.js" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="40" alt="MongoDB" title="MongoDB" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="Git" title="Git" />
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/githubactions/githubactions-original.svg" height="40" alt="GitHub Actions" title="GitHub Actions" />
</p>

## Proyectos destacados

### 🍯 [PFC-Cowrie](https://github.com/diegofonterosa/PFC-Cowrie) · Honeypot SSH con inteligencia de amenazas
Proyecto final de ASIR. Honeypot Cowrie expuesto a Internet en Hetzner durante 28 días y análisis de los ataques capturados.

- **216.222 sesiones** desde 4.028 IP de 119 países
- **24 técnicas MITRE ATT&CK** en 9 tácticas, con clasificador propio en Python (52/52 pruebas)
- Campañas identificadas: botnet Outlaw/Dota, criptominero RedTail y credential stuffing por huella HASSH
- Stack: `Cowrie`, `Python`, `iptables`, `MITRE ATT&CK`, `Wazuh`

### 🔐 [dvwa-devsecops-pipeline](https://github.com/diegofonterosa/dvwa-devsecops-pipeline) · Pipeline DevSecOps
Pipeline en GitHub Actions de cinco fases sobre una aplicación vulnerable (DVWA).

- SAST con Semgrep, SCA con Trivy, secretos con Gitleaks, imagen Docker con Trivy y DAST con OWASP ZAP
- Corrección de SQLi, XSS e inyección de comandos
- Stack: `GitHub Actions`, `Semgrep`, `Trivy`, `Gitleaks`, `OWASP ZAP`, `Docker`

### 🛡️ [Security Alert Monitor](https://github.com/diegofonterosa/security-alert-monitor) · Mini-SIEM
Panel de alertas de seguridad inspirado en mi trabajo en la CRA, con API REST y dashboard web.

- Autenticación JWT, Helmet, CORS y rate limiting
- Vulnerabilidades corregidas tras el análisis con SonarCloud (NoSQL injection, XSS y mass assignment)
- Stack: `Node.js`, `Express`, `MongoDB`, `Chart.js`

### 🌐 [Proyecto-WebStack](https://github.com/diegofonterosa/Proyecto-WebStack) · E-commerce con microservicios
API Gateway en Node.js, servicios en PHP, Strapi CMS y MySQL orquestados con Docker Compose, con CI/CD en GitHub Actions.

- Stack: `Node.js`, `PHP`, `MySQL`, `Docker`, `GitHub Actions`

<details>
<summary><b>Otros proyectos</b></summary>

- [ASIR Interactive Quiz System](https://github.com/diegofonterosa/ASIR-Interactive-Quiz-System): cuestionario CLI en Python con ranking persistente
- [File Manager CLI Python](https://github.com/diegofonterosa/File-Manager-CLI-Python): gestor de archivos desde terminal
- [udemy-free-course-bot](https://github.com/diegofonterosa/udemy-free-course-bot): bot que detecta cursos gratuitos y avisa por Telegram
- [Tienda Gaming Web](https://github.com/diegofonterosa/Proyecto-tienda-gaming-web): tienda online en HTML, CSS y JavaScript
- [Portfolio](https://github.com/diegofonterosa/Portfolio): mi portfolio web personal

</details>

## Ahora mismo

- Cerrando las prácticas (hasta el 15 de diciembre de 2026)
- Defensa del proyecto final de ASIR en diciembre de 2026
- Próximo objetivo de certificación: Azure Administrator (AZ-104)

## Estadísticas GitHub

<p align="center">
  <img src="https://raw.githubusercontent.com/diegofonterosa/diegofonterosa/main/profile-summary-card-output/tokyonight/0-profile-details.svg" alt="Actividad en GitHub de diegofonterosa" />
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/diegofonterosa/diegofonterosa/main/profile-summary-card-output/tokyonight/3-stats.svg" height="170" alt="Estadísticas de GitHub de diegofonterosa" />
  <img src="https://raw.githubusercontent.com/diegofonterosa/diegofonterosa/main/profile-summary-card-output/tokyonight/2-most-commit-language.svg" height="170" alt="Lenguajes con más commits" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=diegofonterosa&theme=tokyonight&hide_border=false" alt="Racha de contribuciones" />
</p>

## Conecta conmigo

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/diegofonterosa)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/diegofonterosa)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:diegofonterosa@gmail.com)

</div>

<p align="center">
  <i>¿Tienes una vacante de SOC, NOC o soporte IT? Escríbeme.</i>
</p>
