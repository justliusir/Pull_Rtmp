import base64
import os, platform

# 设置VLC库路径，需在import vlc之前
os.environ['PYTHON_VLC_MODULE_PATH'] = "./vlc"
video_url="rtmp://media3.scctv.net/live/scctv_800"

import vlc


class Player:
    '''
        args:设置 options
    '''
    instance = vlc.Instance()
    media=instance.media_player_new()

    def __init__(self, *args):
        if args:
            instance = vlc.Instance(*args)
            #self.media = instance.media_player_new()
        else:
            print()
            #self.media = vlc.MediaPlayer()

    # 设置待播放的url地址或本地文件路径，每次调用都会重新加载资源
    def set_uri(self, uri):
        self.media.set_mrl(uri)

    # 播放 成功返回0，失败返回-1
    def play(self, path=None):
        if path:
            self.set_uri(path)
            play=self.media.play()
            print("playing")
            return play
        else:
            return self.media.play()

    # 暂停
    def pause(self):
        self.media.pause()

    # 恢复
    def resume(self):
        self.media.set_pause(0)

    # 停止
    def stop(self):
        self.media.stop()

    # 释放资源
    def release(self):
        return self.media.release()

    # 是否正在播放
    def is_playing(self):
        return self.media.is_playing()

    # 已播放时间，返回毫秒值
    def get_time(self):
        return self.media.get_time()

    # 拖动指定的毫秒值处播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_time(self, ms):
        return self.media.get_time()

    # 音视频总长度，返回毫秒值
    def get_length(self):
        return self.media.get_length()

    # 获取当前音量（0~100）
    def get_volume(self):
        return self.media.audio_get_volume()

    # 设置音量（0~100）
    def set_volume(self, volume):
        return self.media.audio_set_volume(volume)

    # 返回当前状态：正在播放；暂停中；其他
    def get_state(self):
        state = self.media.get_state()
        if state == vlc.State.Playing:
            return 1
        elif state == vlc.State.Paused:
            return 0
        else:
            return -1

    # 当前播放进度情况。返回0.0~1.0之间的浮点数
    def get_position(self):
        return self.media.get_position()

    # 拖动当前进度，传入0.0~1.0之间的浮点数(需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_position(self, float_val):
        return self.media.set_position(float_val)

    # 获取当前文件播放速率
    def get_rate(self):
        return self.media.get_rate()

    # 设置播放速率（如：1.2，表示加速1.2倍播放）
    def set_rate(self, rate):
        return self.media.set_rate(rate)

    # 设置宽高比率（如"16:9","4:3"）
    def set_ratio(self, ratio):
        self.media.video_set_scale(0)  # 必须设置为0，否则无法修改屏幕宽高
        self.media.video_set_aspect_ratio(ratio)

    # 设置窗口句柄
    def set_window(self, wm_id):
        if platform.system() == 'Windows':
            self.media.set_hwnd(wm_id)
        else:
            self.media.set_xwindow(wm_id)

    # 注册监听器
    def add_callback(self, event_type, callback):
        self.media.event_manager().event_attach(event_type, callback)

    # 移除监听器
    def remove_callback(self, event_type, callback):
        self.media.event_manager().event_detach(event_type, callback)



import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        ico = "AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAA9PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/ZFA//4JfQv+CX0L/gl9C/4JfQv+CX0L/gl9C/4JfQv+CX0L/gl9C/4JfQv9iTz//PTw7/z08O/89PDv/TUQ8/5ZpRP92WUH/VUg9/2VQP/9KQjz/SkI8/0pCPP9KQjz/SkI8/0pCPP9KQjz/kmdE/0pCPP89PDv/PTw7/1hJPf+WaUT/WEFH/1g+S/9NPUT/PTxL/z08TP84QUL/MUlG/0pFPf9cSz7/XE07/4BgP/9USD3/PTw7/z08O/9YST3/lmlE/2RQP/9NQz7/Pjw7/z08O/9ZTz//dGNB/4p0RP+Lc0T/SEM8/z49Ov95W0H/VEg9/z08O/89PDv/WEk9/49mRP+udUf/aVI//z08O/89PDv/hm9D/7SQSP/hsE7/4bBO/4hxQ/89PDv/d1lB/1RIPf89PDv/PTw7/1hJPf90WEH/qXNG/2lSP/89PDv/PTw7/5N5RP+0kEj/4bBO/+GwTv+4k0n/PTw7/3dZQf9USD3/PTw7/z08O/9YST3/dFhB/6lzRv/Cf0n/uXtI/3NXQP9JRDz/VEw9/8edSv+Fb0P/UUo9/z08O/93WUH/VEg9/z08O/89PDv/WEk9/3RYQf+pc0b/aVI//0hBPP/Phkv/RUA7/z08O/96Z0L/aFo//z08O/89PDv/fl1C/1FGPf89PDv/PTw7/1hJPf90WEH/qXNG/2lSP/9BPjv/zoZL/5JoRP++h0n/vodJ/76HSf++h0n/voJJ/4liQ/89PDv/PTw7/z08O/9YST3/dFhB/51sRf/Afkn/vn1J/4liQ//DiUr/4bBO/+GwTv/hsE7/4bBO/96dTf9APTv/PTw7/z08O/89PDv/TkQ8/49lRP9KQjz/SkI8/0pCPP9bSz7/vH9J/6x6R/+sekf/rHpH/6x6R/9/XkL/PTw7/z08O/89PDv/PTw7/z08O/9lUD//gl9C/4JfQv+CX0L/fFxB/0M/O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/PTw7/z08O/89PDv/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(ico))
        tmp.close()
        self.geometry('300x300')
        self.iconbitmap("tmp.ico")
        os.remove("tmp.ico")  # 删除icon文件
        self.player = Player()
        self.title("三中电视台直播V1.0.1")
        self.create_video_view()
        self.create_control_view()
        self.player.play(video_url)

    def create_video_view(self):
        self._canvas = tk.Canvas(self, bg="black")
        self._canvas
        self._canvas.pack(fill = 'both',expand ='yes')
        self.player.set_window(self._canvas.winfo_id())

    def create_control_view(self):
        frame = tk.Frame(self)
        tk.Button(frame, text="播放", command=lambda: self.click(0)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="暂停", command=lambda: self.click(1)).pack(side=tk.LEFT)
        tk.Button(frame, text="停止", command=lambda: self.click(2)).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="调试播放（CCTV1）", command=lambda: self.click(3)).pack(side=tk.LEFT, padx=5)
        frame.pack()

    def click(self, action):
        if action == 0:
            if self.player.get_state() == 0:
                self.player.resume()
            elif self.player.get_state() == 1:
                pass  # 播放新资源
            else:
                self.player.play(video_url)
        elif action == 1:
            if self.player.get_state() == 1:
                self.player.pause()
        elif action == 2:
            self.player.stop()
        elif action == 3:
            self.player.play("rtmp://media3.scctv.net/live/scctv_800")


if "__main__" == __name__:
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        app.showwarning(title="警告信息", message="内容")
        #print(e)
