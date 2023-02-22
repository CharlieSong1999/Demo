# Introduction

This is a Demo for the project "Intelligent Manufacturing-oriented Big Data Analytics across the Production Process: Methodologies and Applications"

It allows users to upload the data set for a control parameter recommendation algorithm and a self-adapting trajectory redress algorithm and then demonstrate the result of them.

# Getting Start

It's a project with both the front-end and the back-end, meaning that we have to use two processes serving as a front-end server and a back-end server.

To start the Front-end service, please go to the `/Front-End/` folder.

1. run `npm i`
2. run `npm run dev`

To start the Back-end service, please go to the `/Back-End/` folder.

1. run `pip install -r requirements.txt`
2. run `python api.py`

## Software version

- Python 3.9.15
- npm 8.19.2
- node 18.12.1

# Usage

There are three pages.

![](./img/Data%20Input.png)

The first page allows you to upload your dataset, and then assign them to the corresponding industrial process. Before stepping to the next page, you have to confirm that you have assigned the correct data file to the corresponding process.

![](./img/Control%20Parameter%20Recommendation.png)

The second page demonstrates a control parameter recommendation system of a laser welding process. On the left, you will see a list of numerical input boxes, which allow you to adjust the parameters as you like, click the button below will fill the boxes with our recommended parameter automatically. On the right is the illustration of the physical meaning of the parameter you are now focusing on.

To clarify that we recommend optimum parameter combination, some industrial indicators are showing on the top, making it easier to the comparison between ours and the one you adjected.

![](./img/Trajectory%20self-adapting%20redress.png)

The final page demonstrates a trajectory self-adapting redress algorithm based on an ultra-precise diamond-cutting process. In the graph, the original command position, the redressed command position, and the following error will be depicted as a line graph. There are two types of trajectories to choose from, showing that our algorithm could tackle multiple situations.

# Features

1. Draggable way to input datasets to their corresponding industrial process.
2. Big data-driven Control parameter recommendation algorithm on the laser welding process.
3. Big data-driven Trajectory self-adapting redress algorithm on cutter movement control of the ultra-precision diamond cutting process.

# Development

The demo consists of two parts: Front-End and Back-End.

## Front-End

Using vite + vue3 + typescript + element-ui + draggable as the project-based.

### Project Structure

```bash
.
├── README.md
├── auto-imports.d.ts
├── components.d.ts
├── index.html
├── node_modules
├── package-lock.json
├── package.json
├── public
├── src
│   ├── App.vue
│   ├── assets
│   ├── components
│   │   ├── Draggable
│   │   ├── Echarts
│   │   ├── Form
│   │   ├── Header
│   │   ├── Upload
│   │   └── store
│   ├── main.ts
│   ├── page
│   │   ├── Page1.vue
│   │   ├── Page2.vue
│   │   └── Page3.vue
│   ├── types
│   ├── utilies
│   ├── router
│   ├── api
│   └── vite-env.d.ts
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

### Router

![](./img/router.png)

### API

- Upload:
  - Url: '/api/upload'
  - Method: POST
  - Send: File
  - Receive: JSON
    Front end uses this API to upload the data file to the back-end server. The back-end server will decompress the file and then go through all available data files before returning the list of them.

- getProcesses:
  - Url: '/api/getprocesses'
  - Method: GET
  - Send: None
  - Receive: JSON  
    The end uses this API to get the info on processes available on the back end. Normally it should contain the name of the process and the parameters it required.

- getRecommend:
  - Url: '/api/getRecommend'
  - Method: GET
  - Send: String
  - Receive: Json
    Front end uses this API to get the result of parameter recommendation from the back end. The front end will send the path of the data file to the back end, then the back end will return the result in json form.
- self-adapting:
  - Url: '/api/selfAdapting'
  - Method: GET
  - Send: String
  - Receive: Json
Front end uses this API to get the result of trajectory self-adapting redressment. The front end should tell the back end server the path of the data file, then the back end shall return a list of results in JSON form.

### Draggable Data Input

Please refer to the codes in `/src/components/Draggable`

### Echarts

Please refer to the codes in `/src/components/Echarts`

## Back-End

Using Python + Flask as the back-end server.

Using sk-learn to implement the two algorithms.

### Config

Config files were placed in `config`

### Control Parameter Recommendation

#### Background

Laser beam welding (LBW) is a welding technique used to join pieces of metal or thermoplastics through the use of a laser. The beam provides a concentrated heat source, allowing for narrow, deep welds and high welding rates. The process is frequently used in high volume and precision requiring applications using automation, as in the automotive and aeronautics industries. It is based on keyhole or penetration mode welding.

Since laser beam welding has high power density (on the order of 1 MW/cm2) resulting in small heat-affected zones and high heating and cooling rates, in some control parameter settings, some cracks would occur on the metal, making it a defective product.

Apart from the cracks, some of the parameters have some physical attributes, making it worth optimizing, in order to make the industrial process cost-effective, fast, and flawless.

Considering all the above, we want to propose a control parameter recommendation algorithm, that could recommend the optimal parameter settings while making sure that no cracks would occur on the metal.

**Given**:

- The parameter settings $\lbrace P_i \rbrace_{i=1}^{N}$ where $N$ denotes the number of parameter combinations, and $P_i = (p_1, p_2, \ldots, p_k)$ where $k$ denotes the number of categories of paramters.

- Label set $\lbrace y_i\rbrace_{i=1}^{N}$ where $y_i = [0,1]$ and $0$ denotes there is a crack after welding while $1$ denotes there isn't a crack after welding.

- A set of parameters that should maximize $\lbrace p_{j}\rbrace_{j \in K_1}$, a set of parameters that should minimize $\lbrace p_{j}\rbrace_{j \in K_2}$, and a set of parameters that are no optimization goal $\lbrace p_{j}\rbrace_{j \in K_3}$ where $K_1 \cup K_2 \cup K_3 = K$ and $K_i \cap K_j = \phi, (i \neq j)$

**Objective**

- Output a combination of $(p^{j})_{j=1}^{k}$ that after welding, there wouldn't be any cracks on the metal while meeting all optimization goals.

#### Method

There are six kinds of parameters provided by the data set, that is:

|           Name           | DataType  |    Range     | Step  |
|:-----------------------: |:--------: |:-----------: |:----: |
|        power (W)         |   int64   | [900, 1200]  |   1   |
|  welding speed (m/min)   |  float64  |  [0.8, 1.2]  |  0.1  |
|  gas flow rate (l/min)   |   int64   |   [10, 20]   |   1   |
|   focal position (mm)    |   int64   |   [-2, 2]    |   1   |
|   angular position (°)   |   int64   |  [-15, 15]   |   1   |
| material thickness (mm)  |  float64  |  [0.5, 0.7]  |  0.1  |

And the result is whether there will be a crack in the welding metal afterward.

According to domain knowledge, we assume $K_1 = \lbrace \text{welding speed (m/min)} \rbrace$, $K_2 = \lbrace \text{power (W), gas flow rate (l/min)} \rbrace$, and $K_3 = \lbrace \text{focal position (mm), angular position (°), material thickness (mm)} \rbrace$

1. We use a LogisticRegression model provided by sk-learn to learn a mapping $f(P) \rightarrow \hat y$.
2. We enumerate all possible combinations of parameters $\lbrace P \rbrace_{\text{all}}$ and apply the mapping $f$ on them, from which we select those with $\hat y=1$ as the alternative set $\lbrace P \rbrace_{\text{alt}}$.
3. Finally, we utilize Immune Genetic Algorithm to select the optimal combination $P_{\text{opt}}$ from $\lbrace P \rbrace_{\text{alt}}$ by simultaneously meeting all optimization objectives.

For implementation details please refer to the codes in `laser_welding.py`.

---

### Self-Adapting Trajectory Control

#### Background

Ultra-precision cutting starts with SPDT (SinglePoint Diamond Turning) technology, which is supported by air-bearing spindles, pneumatic slides, high rigidity, high precision tools, feedback control and ambient temperature control to achieve nanoscale surface roughness. Diamond cutters are mostly used for milling, which is widely used in the processing of copper plane and aspherical optical components, plexiglass, plastic products (such as plastic lenses for cameras, contact lens lenses, etc.), ceramics and composite materials.

Among the supporting technologies, feedback control is the technology we want to discuss in this case. Feedback control is a control mechanism that uses information from measurements to manipulate a variable to achieve the desired result. The objective is to develop a model or algorithm governing the application of system inputs to drive the system to a desired state, while minimizing any delay, overshoot, or steady-state error and ensuring a level of control stability; often with the aim to achieve a degree of optimality.

To do this, a controller with the requisite corrective behavior is required. This controller monitors the controlled process variable (PV), and compares it with the reference or set point (SP). The difference between the actual and desired value of the process variable, called the error signal, or SP-PV error, is applied as feedback to generate a control action to bring the controlled process variable to the same value as the set point.

#### Problem Setting

**Given**

- A sequence of set points $S^{h}$, in this case, named as command position.
- A Sequence of actual points $A^{h}$, i.e., the result points of the industrial process after input $S^{h}$ directly.

**Objective**

- To find another set points $S^{m}$, which could get $A^{m}$ as a result, while satisfy that $A^{m} \sim S^{h}$

#### Method

It's natural that there exists a mapping $f$ that $f(S^h) \rightarrow A^h$. We could find one of its inverse mappings that satisfies $f^{-1}(A^h) \rightarrow S^h$, meaning that with $A^h$ as the result we could predict the original command points. Then we could input $S^h$ to get $S^{m}$, which is supposed to be the command points that could consequence $S^h$.

In practical, we directly learn $f^{-1}$ with $S^h$ and $A^h$, then use the output of $f^{-1}(S^h)$ as the algorithm output.

For more details, please refer to the codes in `self_adapting.py`.
