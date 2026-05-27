import json
from flask import make_response
from db import db
from models.jogo_models import Jogo

def get_jogos():
    jogos = Jogo.query.all()
    jogos_json = [jogo.json() for jogo in jogos]
    response = make_response(json.dumps(jogos_json, ensure_ascii=False, sort_keys=False))
    response.headers['Content-Type'] = 'application/json'
    return response

def get_jogo_by_id(jogo_id):
    jogo = Jogo.query.get(jogo_id)
    if jogo:
        response = make_response(json.dumps(jogo.json(), ensure_ascii=False, sort_keys=False))
    else:
        response = make_response(json.dumps({'mensagem': 'Jogo não encontrado.'}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json'
    return response

def create_jogo(jogo_data):
    novo_jogo = Jogo(
        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        desenvolvedor=jogo_data['desenvolvedor'],
        plataforma=jogo_data['plataforma']
    )
    db.session.add(novo_jogo)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Jogo cadastrado com sucesso.',
            'jogo': novo_jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response

def update_jogo(jogo_id, jogo_data):
    jogo = Jogo.query.get(jogo_id)
    if jogo:
        jogo.titulo = jogo_data['titulo']
        jogo.genero = jogo_data['genero']
        jogo.desenvolvedor = jogo_data['desenvolvedor']
        jogo.plataforma = jogo_data['plataforma']
        db.session.commit()
        response = make_response(json.dumps(jogo.json(), ensure_ascii=False, sort_keys=False))
    else:
        response = make_response(json.dumps({'mensagem': 'Jogo não encontrado.'}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json'
    return response

def delete_jogo(jogo_id):
    jogo = Jogo.query.get(jogo_id)
    if jogo:
        db.session.delete(jogo)
        db.session.commit()
        response = make_response(json.dumps({'mensagem': f'Jogo {jogo_id} excluído com sucesso.'}, ensure_ascii=False))
    else:
        response = make_response(json.dumps({'mensagem': 'Jogo não encontrado.'}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json'
    return response
