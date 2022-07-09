from flask_restful import Resource, reqparse


class Video(Resource):
    def get(self, video_id):
        return 'hello world!', 200

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}, 201


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='name of the video')
video_put_args.add_argument('views', type=int, help='views of the video')
video_put_args.add_argument('likes', type=int, help='likes on the video')
