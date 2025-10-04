<<<<<<< HEAD
import json
import asyncio
import time
from datetime import datetime

class CollaborationAdapter:
    def __init__(self):
        self.active_sessions = {}
        self.user_presence = {}
        self.collaboration_history = []
    
    def create_collaboration_session(self, session_id, owner, project_context):
        session = {
            "session_id": session_id,
            "owner": owner,
            "participants": [owner],
            "project_context": project_context,
            "created_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "active_file": None,
            "cursor_positions": {},
            "edits": []
        }
        
        self.active_sessions[session_id] = session
        self.user_presence[owner] = session_id
        
        return session
    
    def join_session(self, session_id, user):
        if session_id not in self.active_sessions:
            return {"error": "Session not found"}
        
        session = self.active_sessions[session_id]
        
        if user not in session["participants"]:
            session["participants"].append(user)
        
        self.user_presence[user] = session_id
        session["last_activity"] = datetime.now().isoformat()
        
        return session
    
    def update_cursor_position(self, session_id, user, file_path, line, column):
        if session_id not in self.active_sessions:
            return {"error": "Session not found"}
        
        session = self.active_sessions[session_id]
        
        if "cursor_positions" not in session:
            session["cursor_positions"] = {}
        
        session["cursor_positions"][user] = {
            "file": file_path,
            "line": line,
            "column": column,
            "timestamp": datetime.now().isoformat()
        }
        
        session["last_activity"] = datetime.now().isoformat()
        
        return session
    
    def record_edit(self, session_id, user, edit_data):
        if session_id not in self.active_sessions:
            return {"error": "Session not found"}
        
        edit_record = {
            "user": user,
            "timestamp": datetime.now().isoformat(),
            "data": edit_data,
            "edit_id": f"edit_{len(self.collaboration_history) + 1}"
        }
        
        self.active_sessions[session_id]["edits"].append(edit_record)
        self.collaboration_history.append(edit_record)
        
        self.active_sessions[session_id]["last_activity"] = datetime.now().isoformat()
        
        return edit_record
    
    def get_session_state(self, session_id):
        if session_id not in self.active_sessions:
            return {"error": "Session not found"}
        
        return self.active_sessions[session_id]
    
    def get_user_presence(self, user):
        return self.user_presence.get(user)
    
    def generate_collaboration_metrics(self):
        active_users = len(self.user_presence)
        active_sessions = len(self.active_sessions)
        total_edits = len(self.collaboration_history)
        
        recent_edits = [e for e in self.collaboration_history 
                       if (datetime.now() - datetime.fromisoformat(e['timestamp'])).seconds < 3600]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "active_users": active_users,
            "active_sessions": active_sessions,
            "total_edits": total_edits,
            "recent_activity": len(recent_edits),
            "collaboration_health": self.assess_collaboration_health(active_users, active_sessions)
        }
    
    def assess_collaboration_health(self, active_users, active_sessions):
        if active_users == 0:
            return "inactive"
        elif active_users >= 10 and active_sessions >= 3:
            return "thriving"
        elif active_users >= 3 and active_sessions >= 1:
            return "active"
        else:
            return "developing"

collaboration_adapter = CollaborationAdapter()
=======
class CollaborationAdapter:
    def __init__(self):
        self.active_sessions = {}
    
    def create_collaboration_session(self, session_id, owner):
        return {"session_id": session_id}

collaboration_adapter = CollaborationAdapter()
>>>>>>> db7bc0e26d01433233b05f14b13fb73dbca52f97
