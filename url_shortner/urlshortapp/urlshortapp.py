from flask import render_template, request, redirect, url_for, flash, send_from_directory, abort, session,jsonify, Blueprint
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename

bp = Blueprint('urlshortapp', __name__)

print(__name__)

@bp.route('/')
def home():
    print("Request Method in home is : ", request.method)
    return render_template('home.html', name="Rupesh", code=session.items())

@bp.route('/your_url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        # print("request is : ", request)
        # print("request.form is : ", request.form)
        # print("request.form.keys() : ",request.form.keys())
        # print("request.form.values() : ",request.form.values())
        # print("request.files : ",request.files)
        # print("request.files.keys() : ",request.files.keys())
        # print("request.files.values() : ", request.files.values())
        # print('URL is  : ', request.form['url'])
        # print("Code is : ", request.form['code'])
        # print("File Object is : ",request.files['file'])
        # print("File Name is : ", request.files['file'].filename)
        # print("Request Method is : ",request.method)
        
        urls = {}
        
        # Check if urls.json exists and load its contents
        if os.path.exists('urls.json'):
            with open('urls.json', 'r') as urls_file:
                urls = json.load(urls_file)
                
        # Check if the code already exists
        if request.form['code'] in urls.keys():
            # Flashes a message to the next request. In order to remove the flashed message from the session and to display it to the user, the template has to call get_flashed_messages
            flash(message="The Code already exists, please choose another code", category='info')
            return redirect(url_for('urlshortapp.home'))
        
        # Now, we need to check if the incoming request is 'url' or a 'file'
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url' : request.form['url']}
        else:
            print("Getting the File Name : ")
            file_name = request.files['file']
            print(file_name)
            full_file_name = request.form['code'] + '_'+ secure_filename(file_name.filename)
            print(full_file_name)
            # The error occurs because backslashes (\) in strings can be interpreted as escape sequences in Python. 
            # To avoid this, you have a few options: 1: Use Raw Strings  2: Replace Backslashes with Forward Slashes
            file_name.save(r'C:\Users\Santosh\Desktop\LearnFlask\url_shortner\urlshortapp\static\user_files\\' + full_file_name)
            
            # update the urls.json dictionary
            urls[request.form['code']] = {'file' : full_file_name}
            
        # Save the updated dictionary back to urls.json
        with open('urls.json', 'w') as urls_file:
            json.dump(urls, urls_file)
            date_time = datetime.now()
            session[request.form['code']] = date_time
        return render_template('your_url.html', code = request.form['code'])
    else:
        print("Hello, i am home again")
        return redirect(url_for('urlshortapp.home'))
        # print(request.args)
        '''
        In your code, you're trying to access request.args['url'] and request.args['code'] in the GET request to /your_url. 
        However, if you access /your_url directly from your browser without providing any query parameters, these keys (url and code) do not exist, leading to a KeyError.
        request.args.get('url') and request.args.get('code') will safely return None if the keys are not present, preventing a KeyError
        '''
        # print('URL is  : ', request.args['url'])
        # print("Code is : ", request.args['code'])
   
        # Use `.get()` to avoid KeyError
        # print(request.args)
        # url = request.args.get('url')
        # code = request.args.get('code')
        # print('URL is  : ', url)
        # print("Code is : ", code)
        # print("Request Method is : ", request.method)
        

@bp.route('/<string:code>')
def redirect_to_url_from_code(code):
    if os.path.exists('urls.json'):
        with open('urls.json','r') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    # file_name = urls[code]['file']
                    # print("file_name is : ", file_name)
                    # file_path  = 'C:Users/Santosh/Desktop/LearnFlask/static/user_files/' 
                    # print("file_path is : ", file_path)
                    # return send_from_directory(directory=file_path, path=file_name)
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404


@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))



if __name__ == "__main__":
    bp.run(debug=True, use_reloader=True)
