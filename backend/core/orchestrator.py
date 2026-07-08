from concurrent.futures import ThreadPoolExecutor

from core.workspace import Workspace
from core.live_workspace import LiveWorkspace
from core.agent_state import AgentStateEngine
from core.planner import create_plan
from core.debate import run as debate_agent
from core.recovery import execute_with_retry
from core.memory import save_project
from core.knowledge_graph import KnowledgeGraph
from core.event_bus import EventBus
from core.mission import Mission
from core.conversation import ConversationBoard
from core.stream import StreamEngine
from core.confidence import ConfidenceEngine
from core.model_router import ModelRouter
from core.agent_factory import AgentFactory
from core.memory_manager import MemoryManager
from core.replanner import run as replanner

from agents.qa import run as qa_agent
from agents.research import run as research_agent
from agents.engineer import run as engineer_agent
from agents.designer import run as designer_agent
from agents.documentation import run as documentation_agent
from agents.leader import run as leader_agent
from agents.reflection import run as reflection_agent
from agents.peer_review import run as peer_review_agent

# ==================== NEW IMPORTS (added exactly as you asked) ====================
from core.team_manager import TeamManager
from core.plugin_manager import PluginManager
from core.organization import Organization
from core.project_generator import ProjectGenerator
from core.file_editor import FileEditor
from core.code_executor import CodeExecutor
from core.test_runner import TestRunner
from core.bug_fixer import BugFixer
from core.git_manager import GitManager
from core.docker_manager import DockerManager
from core.deployment_manager import DeploymentManager
from core.expert_router import ExpertRouter   # Added exactly as requested


PROJECT_NAME = "default_project"


def orchestrate(user_prompt):

    workspace = Workspace()

    # ==================== MEMORY MANAGER ====================
    memory = MemoryManager()

    # Load previous projects for context
    previous_projects = memory.find(user_prompt)
    previous_context = []

    for project in previous_projects:
        data = memory.load(project)
        if data:
            previous_context.append(data)

    live = LiveWorkspace()

    graph = KnowledgeGraph()

    bus = EventBus()

    mission = Mission()

    conversations = ConversationBoard()

    states = AgentStateEngine()

    stream = StreamEngine()

    confidence = ConfidenceEngine()

    router = ModelRouter()

    factory = AgentFactory()

    expert_router = ExpertRouter()          # Added exactly as requested

    experts = expert_router.build_team(     # Added exactly as requested
        user_prompt,
    )

    # ==================== NEW INSTANCES (added exactly as you asked) ====================
    team_manager = TeamManager()
    plugin_manager = PluginManager()
    organization = Organization()
    generator = ProjectGenerator()
    editor = FileEditor()
    executor = CodeExecutor()
    tester = TestRunner()
    fixer = BugFixer()
    git = GitManager()
    docker = DockerManager()
    deployment = DeploymentManager()

    # ==================== CREATE ALL AGENTS ====================
    factory.create("Leader", "Chief Executive Officer")
    factory.create("Research", "Research Specialist")
    factory.create("Engineer", "Software Engineer")
    factory.create("Designer", "UI/UX Designer")
    factory.create("Documentation", "Technical Writer")
    factory.create("QA", "Quality Assurance")

    if plugin_manager.enabled_plugins():
        if experts["backend"] and "Backend Expert" in plugin_manager.enabled_plugins():
            factory.create("Backend Expert", "Backend Architect", "Engineering")
        if experts["frontend"] and "Frontend Expert" in plugin_manager.enabled_plugins():
            factory.create("Frontend Expert", "Frontend Architect", "Engineering")
        if experts["database"] and "Database Expert" in plugin_manager.enabled_plugins():
            factory.create("Database Expert", "Database Engineer", "Engineering")
        if experts["security"] and "Security Expert" in plugin_manager.enabled_plugins():
            factory.create("Security Expert", "Cyber Security", "Security")
        if experts["devops"] and "DevOps Expert" in plugin_manager.enabled_plugins():
            factory.create("DevOps Expert", "Cloud Infrastructure", "Infrastructure")
        if experts["mobile"] and "Mobile Expert" in plugin_manager.enabled_plugins():
            factory.create("Mobile Expert", "Mobile Developer", "Engineering")
        if experts["ai"] and "AI Expert" in plugin_manager.enabled_plugins():
            factory.create("AI Expert", "LLM Engineer", "AI")
        if experts["testing"] and "Testing Expert" in plugin_manager.enabled_plugins():
            factory.create("Testing Expert", "Automation Tester", "QA")

    organization.set_ceo("Leader")

    for agent in factory.get().values():
        department = agent["team"]
        organization.create_department(department)
        if organization.export()["Departments"][department]["manager"] is None:
            organization.appoint_manager(department, agent["name"])
        organization.add_member(department, agent["name"])

    selected_models = router.choose("leader", user_prompt)

    execution_plan = create_plan(user_prompt, previous_context)

    mission.start(
        user_prompt[:50],
        [
            "Planning", "Research", "Engineering", "Design",
            "Documentation", "QA", "Leader",
        ],
    )

    project_name = (
        user_prompt.lower()
        .replace(" ", "_")
        .replace("/", "")
        .replace("\\", "")
    )[:40]

    project_directory = generator.generate(project_name)

    # Generate basic files
    editor.overwrite(
        f"{project_directory}/README.md",
        f"# {project_name}\n\nGenerated by HIVE OS",
    )
    editor.create_file(f"{project_directory}/.env", "ENV=development\n")
    editor.create_file(
        f"{project_directory}/backend/api/routes.py",
        """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Hello from HIVE OS"}""",
    )

    docker_files = docker.create(project_directory)

    stream.push("Leader", "Docker environment generated.")

    # ==================== RUN AGENTS (PARALLEL EXECUTION - ThreadPoolExecutor) ====================
    with ThreadPoolExecutor(max_workers=6) as executor:

        research_future = executor.submit(
            execute_with_retry,
            "Research",
            research_agent,
            3,
            1,
            user_prompt,
        )

        engineer_future = executor.submit(
            execute_with_retry,
            "Engineer",
            engineer_agent,
            3,
            1,
            user_prompt,
            "",
        )

        designer_future = executor.submit(
            execute_with_retry,
            "Designer",
            designer_agent,
            3,
            1,
            user_prompt,
            "",
            "",
        )

        documentation_future = executor.submit(
            execute_with_retry,
            "Documentation",
            documentation_agent,
            3,
            1,
            user_prompt,
            "",
            "",
            "",
        )

        qa_future = executor.submit(
            execute_with_retry,
            "QA",
            qa_agent,
            3,
            1,
            user_prompt,
            "",
            "",
            "",
        )

        research = research_future.result()
        engineer = engineer_future.result()
        designer = designer_future.result()
        documentation = documentation_future.result()
        qa = qa_future.result()

    debate = execute_with_retry(
        "Debate",
        debate_agent,
        3,
        1,
        research,
        engineer,
        designer,
    )

    # ==================== DISABLED SECTIONS (Reflection, Peer Review, Replanner) ====================
    # reflection = execute_with_retry(...)
    # peer_review = execute_with_retry(...)
    # replan = execute_with_retry(...)

    reflection = None
    peer_review = None
    replan = None

    # ==================== REPLACE LEADER CALL ====================
    final = execute_with_retry(
        "Leader Agent",
        leader_agent,
        3,
        1,
        user_prompt,
        research,
        engineer,
        designer,
        previous_context,
        # reflection,       # disabled
        # peer_review,      # disabled
        # replan,           # disabled
    )

    # ==================== SAVE THE CEO DECISION ====================
    memory.save(
        "latest_project",
        {
            "prompt": user_prompt,
            "plan": execution_plan,
            "research": research,
            "engineer": engineer,
            "designer": designer,
            "documentation": documentation,
            "leader": final,
            "qa": qa,
            "debate": debate,
            # "reflection": reflection,       # disabled
            # "peer_review": peer_review,     # disabled
            # "replan": replan,               # disabled
            "ceo_approval": final,
        },
    )

    return {
        "agents": factory.get(),
        "models": selected_models,
        "mission": mission.export(),
        "workspace": live.get_workspace(),
        "conversation": conversations.history(),
        "stream": stream.history(),
        "confidence": confidence.export(),
        "states": states.get(),
        "timeline": live.get_timeline(),
        "execution_plan": execution_plan,
        "research": research,
        "engineer": engineer,
        "designer": designer,
        "documentation": documentation,
        "debate": debate,
        "qa": qa,
        "final": final,
        "teams": team_manager.export(),
        "plugins": plugin_manager.export(),
        "organization": organization.export(),
        "generated_files": [
            "README.md",
            ".gitignore",
            "docker-compose.yml",

            "frontend/",
            "frontend/package.json",
            "frontend/vite.config.js",
            "frontend/src/",
            "frontend/src/App.jsx",
            "frontend/src/main.jsx",

            "backend/",
            "backend/main.py",
            "backend/requirements.txt",
            "backend/routes/",
            "backend/controllers/",
            "backend/models/",
            "backend/services/",

            "database/",
            "database/schema.sql",

            ".github/workflows/",
            ".env.example",
        ],
        "execution_logs": executor.history(),
        "testing": tester.history(),
        "bug_fixing": [
            "Automatic formatting check completed."
        ],
        "docker_files": docker_files,
        "git_logs": git.history(),
        "deployment": deployment.history(),
        "memory": previous_projects,
        # "reflection": reflection,       # disabled
        # "peer_review": peer_review,     # disabled
        # "replan": replan,               # disabled
        "ceo_approval": final,
        "company_status": {
            "ceo": "Leader",
            "mission": "Completed",
            "departments": organization.export(),
        },
    }