import streamlit as st
from supabase import create_client, Client
import os

@st.cache_resource
def init_supabase_client():
    url: str = "https://pdotihhbofuusnrbchyd.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBkb3RpaGhib2Z1dXNucmJjaHlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA3NjAyNTksImV4cCI6MjA1NjMzNjI1OX0.4G26QaN4n7MeB9HCq1TIvkfmzjVHg1Y4YZg7OWvIOq8"
    supabase: Client = create_client(url, key)
    return supabase

supabase = init_supabase_client()

def check_instructor_credentials(email, password):
    response = supabase.from_('Agents').select("*").eq('email', email).eq('is_instructor', True).execute()
    instructor = response.data
    if instructor and instructor[0]['password'] == password:
        return instructor[0]
    return None

def get_agents():
    response = supabase.from_('Agents').select("*").execute()
    agents = response.data
    return agents

def get_activities():
    response = supabase.from_('Activities').select("*").execute()
    activities = response.data
    return activities

def get_scheduled_activities():
    response = supabase.from_('ScheduledActivities').select("*, Activities(name), Agents(first_name, last_name)").execute()
    scheduled_activities = response.data
    return scheduled_activities

def get_agent_assignments():
    response = supabase.from_('AgentAssignments').select("*").execute()
    agent_assignments = response.data
    return agent_assignments
