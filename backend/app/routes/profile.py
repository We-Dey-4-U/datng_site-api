from flask import Blueprint, request, jsonify
from app.services.profile import create_profile, get_profile_by_user_id, update_profile, delete_profile
from app import db

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/create_profile', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')
    bio = data.get('bio')
    interests = data.get('interests')
    profile_picture_url = data.get('profile_picture_url')
    location = data.get('location')

    try:
        create_profile(user_id, first_name, last_name, age, bio, interests, profile_picture_url, location)
        return jsonify({'message': 'Profile created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@profile_blueprint.route('/get_profile/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    profile = get_profile_by_user_id(user_id)

    if profile:
        return jsonify({
            'user_id': profile.user_id,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'age': profile.age,
            'bio': profile.bio,
            'interests': profile.interests,
            'profile_picture_url': profile.profile_picture_url,
            'location': profile.location,
            'created_at': str(profile.created_at)
        })
    else:
        return jsonify({'error': 'Profile not found'}), 404

@profile_blueprint.route('/update_profile/<int:user_id>', methods=['PATCH'])
def update_user_profile(user_id):
    data = request.get_json()

    try:
        update_profile(user_id, data)
        return jsonify({'message': 'Profile updated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@profile_blueprint.route('/delete_profile/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    try:
        delete_profile(user_id)
        return jsonify({'message': 'Profile deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

# ... you can add more routes as needed ...