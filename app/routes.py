"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

# Game Types
@main_bp.route('/human_vs_human', methods=['GET', 'POST'])
@main_bp.route('/human_vs_computer', methods=['GET', 'POST'])
@main_bp.route('/computer_vs_computer', methods=['GET', 'POST'])

# Player Behavior
@main_bp.route('/player_profile/<int:user_id>', methods=['GET', 'POST'])
@main_bp.route('/player_settings/<int:user_id>', methods=['GET', 'POST'])

# Move Stats
@main_bp.route('/best_first_move', methods=['GET'])
@main_bp.route('/best_second_move', methods=['GET'])
@main_bp.route('/move_history/<int:user_id>', methods=['GET'])

# Training Data Collection
@main_bp.route('/record_game', methods=['POST'])
@main_bp.route('/export_training_data', methods=['GET'])
