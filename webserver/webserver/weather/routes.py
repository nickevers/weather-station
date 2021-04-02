from flask import Blueprint, render_template, request, Response
from flask import current_app as app
from .weather_service import service

# Blueprint Configuration
weather_bp = Blueprint(
    'weather_bp', __name__,
)
  
@weather_bp.route('/current', methods=['GET'])
def get_current():
  data = service.get_current_weather()
  return Response(data, status=202, mimetype='application/json')

@weather_bp.route('/current', methods=['POST'])
def update_current():
  try:
    content = request.get_json()
    service.update_weather(content)
    return Response(status=202)
  except:
    return Response(status=500)


@weather_bp.route('/archive', methods=['POST'])
def save_archive():
  try:
    content = request.get_json()
    service.archive_weather(content)
    return Response(status=202)
  except Exception as e:
    print(e)
    return Response(status=500)

  
  

    