// must define the type and apply it to `focus_id_2_img`
// otherwise it would warn that
// 'Element implicitly has an 'any' type because expression of type 'number' can't be used to index type'
export interface n2s {
  [index: number]: string;
}

export type input_change_type = {
  name: string;
  value: number;
};

export interface r_param {
  [index: string]: number;
}

export interface selfAdapting {
  result: selfAdaptingResult;
}

export interface State {
  data_list: [];
  processes_list: process_item[];
  Flags: Flags;
  Status: Status;
  self_Adapting: selfAdapting;
  recommend_param: r_param;
}

export type param_item = {
  name: string;
  param: [];
  value: number;
  min: number;
  max: number;
  step: number;
};

export type process_item = {
  name: string;
  params: param_item[];
  param_file: string[];
};

export interface selfAdaptingResult {
  [index: string]: { [index: string]: [number[]] };
}

export interface Flags {
  Processes: boolean;
  Upload: boolean;
  Recommend: boolean;
  selfAdapting: boolean;
}

export interface Status {
  Btn_recommend_loading: boolean;
  Page: number;
}
