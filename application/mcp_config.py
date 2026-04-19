import logging
import sys
import utils
import os

logging.basicConfig(
    level=logging.INFO,  # Default to INFO level
    format='%(filename)s:%(lineno)d | %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger("mcp-config")

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

config = utils.load_config()
logger.info(f"config: {config}")

region = config["region"] if "region" in config else "us-west-2"
projectName = config["projectName"] if "projectName" in config else "mcp"
workingDir = os.path.dirname(os.path.abspath(__file__))
# 상위 디렉토리의 contents 폴더 경로 추가
parent_dir = os.path.dirname(workingDir)
contents_dir = os.path.join(parent_dir, "contents")
logger.info(f"workingDir: {workingDir}")
logger.info(f"contents_dir: {contents_dir}")

mcp_user_config = {}    

def load_config(mcp_type):
    if mcp_type == "knowledge base":
        mcp_type = "kb-retriever"
    elif mcp_type == "aws documentation":
        mcp_type = "aws-documentation"    
    elif mcp_type == "trade info":
        mcp_type = "trade-info"
    elif mcp_type == "weather":
        mcp_type = "korea-weather"
    
    if mcp_type == "tavily":
        return {
            "mcpServers": {
                "tavily-search": {
                    "command": "python",
                    "args": [
                        f"{workingDir}/mcp_server_tavily.py"
                    ]
                }
            }
        }
    
    elif mcp_type == "korea-weather":
        return {
            "mcpServers": {
                "korea-weather": {
                    "command": "python",
                    "args": [f"{workingDir}/mcp_server_korea_weather.py"]
                }
            }
        }
        
    elif mcp_type == "kb-retriever":
        return {
            "mcpServers": {
                "kb-retriever": {
                    "command": "python",
                    "args": [f"{workingDir}/mcp_server_retrieve.py"]
                }
            }
        }
    
    elif mcp_type == "aws-documentation":
        return {
            "mcpServers": {
                "awslabs.aws-documentation-mcp-server": {
                    "command": "uvx",
                    "args": ["awslabs.aws-documentation-mcp-server@latest"],
                    "env": {
                        "FASTMCP_LOG_LEVEL": "ERROR"
                    }
                }
            }
        }

    elif mcp_type == "trade-info":
        return {
            "mcpServers": {
                "trade-info": {
                    "command": "python",
                    "args": [
                        f"{workingDir}/mcp_server_trade_info.py"
                    ]
                }
            }
        }    
    
    elif mcp_type == "web_fetch":
        return {
            "mcpServers": {
                "web_fetch": {
                    "command": "npx",
                    "args": ["-y", "mcp-server-fetch-typescript"]
                }
            }
        }
    
    elif mcp_type == "사용자 설정":
        return mcp_user_config

def load_selected_config(mcp_servers: dict):
    logger.info(f"mcp_servers: {mcp_servers}")
    
    loaded_config = {}
    for server in mcp_servers:
        config = load_config(server)
        if config:
            loaded_config.update(config["mcpServers"])
    return {
        "mcpServers": loaded_config
    }
