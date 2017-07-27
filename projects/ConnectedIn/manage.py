#!/usr/bin/env python
import os
import sys


"""
Checklist da atividade 1
[X] - Alterar senha
[X] - Recuperar senha
[X] - Bloquear usuario
[X] - Incluir postagem
[X] - Usuario com foto
[X] - Postagens com foto
[X] - * - Ver lista de pessoas bloqueadas
[X] - * - Editar postagem
[X] - * - Ver suas próprias postagens no perfil
[X] - Exibir timeline
[X] - Excluir perfis (superuser)
[X] - Excluir postagem (superuser)
[X] - Desativar/ativar proprio perfil
[X] - Pagina para superuser
[X] - Conceder privilegio de superuser a outro usuario
[X] - Novo layout
[ ] - Pesquisar usuario
[ ] - * - Usuario poder editar seu perfil
"""

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connectedin.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
